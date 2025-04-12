import json

def process_search_index(json_file, output_file):
    """
    Process the search_index.json file to update blog post locations and titles.

    Args:
        json_file (str): Path to the input search_index.json file.
        output_file (str): Path to save the updated search_index.json file.
    """
    with open(json_file, 'r', encoding='utf-8') as file:
        search_index = json.load(file)

    for entry in search_index["docs"]:
        if "location" in entry and entry["location"].startswith("blog/old_bitcraze_blogposts/"):
            # Replace 'blog/old_bitcraze_blogposts/' with 'https://www.bitcraze.io/'
            entry["location"] = entry["location"].replace("blog/old_bitcraze_blogposts/", "https://www.bitcraze.io/")
            # Replace underscores with slashes
            entry["location"] = entry["location"].replace("_", "/")
            
            # Update the title to remove the date and append Font Awesome icon
            if "title" in entry:
                title_parts = entry["title"].split(" ", 3)  # Split into at most 4 parts
                if len(title_parts) > 3:
                    title_without_date = title_parts[3]
                    entry["title"] = title_without_date.capitalize() + " <i class='fa-solid fa-arrow-up-right-from-square'></i>"
                else:
                    entry["title"] = entry["title"].capitalize() + " <i class='fa-solid fa-arrow-up-right-from-square'></i>"

    # Write the updated search index back to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(search_index, file, indent=4, ensure_ascii=False)

def main():
    # File paths
    json_file = '_site/search/search_index.json'  # Path to the search_index.json file
    output_file = '_site/search/search_index.json'  # Path to save the updated file

    # Process the search index
    process_search_index(json_file, output_file)
    print(f"Processed search index saved to {output_file}")

if __name__ == "__main__":
    main()