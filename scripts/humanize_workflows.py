import os
import json
import re
import sys


def humanize_workflows(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)

            try:
                with open(filepath, "r") as f:
                    data = json.load(f)

                workflow_name = data.get("name", "unnamed_workflow")

                # Slugify the name: remove special chars, replace spaces with underscores
                clean_name = (
                    re.sub(r"[^\w\s-]", "", workflow_name).strip().replace(" ", "_")
                )
                new_filename = f"{clean_name}.json"
                new_filepath = os.path.join(directory, new_filename)

                # Avoid renaming if names are already the same or target exists
                if filepath != new_filepath:
                    print(f"Renaming {filename} -> {new_filename}")
                    os.rename(filepath, new_filepath)

            except Exception as e:
                print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "workflows"
    humanize_workflows(target_dir)
