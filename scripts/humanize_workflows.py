import os
import json
import re
import sys
import argparse


def sanitize_workflow(data):
    """Recursively strip sensitive info from n8n workflow JSON."""
    if isinstance(data, dict):
        # Remove personal metadata
        if "shared" in data:
            data["shared"] = []

        # Recurse into all keys
        for key, value in data.items():
            data[key] = sanitize_workflow(value)
    elif isinstance(data, list):
        data = [sanitize_workflow(item) for item in data]
    elif isinstance(data, str):
        # Mask emails
        data = re.sub(
            r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "[EMAIL_HIDDEN]", data
        )
        # Mask personal names if they appear in strings
        data = data.replace("Navneet Singh Arora", "User")
        data = data.replace("Navneet", "User")
    return data


def process_workflows(directory, should_sanitize=False, target_name=None):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            # Selective filtering
            if target_name and target_name not in filename:
                continue

            filepath = os.path.join(directory, filename)

            try:
                with open(filepath, "r") as f:
                    data = json.load(f)

                # Check if the workflow is archived
                if data.get("isArchived") is True:
                    print(f"Removing archived workflow: {filename} ({data.get('name')})")
                    os.remove(filepath)
                    continue

                if should_sanitize:
                    print(f"Sanitizing {filename}...")
                    data = sanitize_workflow(data)

                workflow_name = data.get("name", "unnamed_workflow")

                # Slugify the name: remove special chars, replace spaces and underscores with hyphens
                clean_name = (
                    re.sub(r"[^\w\s-]", "", workflow_name).strip().replace(" ", "-").replace("_", "-")
                )
                # Ensure no double hyphens from previous conversion
                clean_name = re.sub(r"-+", "-", clean_name)
                new_filename = f"{clean_name}.json"
                new_filepath = os.path.join(directory, new_filename)

                # Always write back to ensure pretty printing and potential sanitization
                with open(new_filepath if filepath != new_filepath else filepath, "w") as f:
                    json.dump(data, f, indent=2)

                # Handle renaming
                if filepath != new_filepath:
                    if os.path.exists(new_filepath):
                        print(f"Warning: {new_filename} already exists. Overwriting.")
                    print(f"Renaming {filename} -> {new_filename}")
                    if os.path.exists(filepath):
                        os.remove(filepath)

            except Exception as e:
                print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Humanize and/or sanitize n8n workflows.")
    parser.add_argument("directory", nargs="?", default="workflows", help="Directory containing workflows")
    parser.add_argument("--sanitize", action="store_true", help="Enable sanitization (stripping personal data)")
    parser.add_argument("--name", help="Specific workflow name to target")
    
    args = parser.parse_args()
    process_workflows(args.directory, args.sanitize, args.name)
