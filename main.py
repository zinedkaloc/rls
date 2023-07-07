import os
import json

# Array to store the changelog data
changelog_data = []

# Walk through the directory
for root, dirs, files in os.walk("./"):
    for file in files:
        # Look for package.json files
        if file == "package.json":
            package_file_path = os.path.join(root, file)
            # Open package.json file
            with open(package_file_path) as json_file:
                data = json.load(json_file)
                # If version and name exists, append it to the changelog data
                if "name" in data and "version" in data:
                    changelog_data.append({
                        'name': data['name'],
                        'version': data['version']
                    })

# Save the changelog data in a json file to be used later in the workflow
with open('changelog_data.json', 'w') as outfile:
    json.dump(changelog_data, outfile)
