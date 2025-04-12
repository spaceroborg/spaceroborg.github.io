from collections import Counter

def define_env(env):
    # A global Counter to store skill occurrences
    env.variables['skill_counts'] = Counter()

    # Load skills from the skills.txt file
    skills_file = "docs/skills.txt"
    try:
        with open(skills_file, "r", encoding="utf-8") as f:
            for line in f:
                skill = line.strip()
                if skill:  # Ignore empty lines
                    env.variables['skill_counts'][skill] += 1
    except FileNotFoundError:
        print(f"Warning: {skills_file} not found. No skills loaded.")

    @env.macro
    def skill_label(skill):
        """Generate a clickable skill label linking to the current page with a search query."""
        from urllib.parse import quote_plus
        skill_slug = quote_plus(skill)  # URL-safe skill name
        env.variables['skill_counts'][skill] += 1  # Increment the skill count
        return f'<a href="?q={skill_slug}" class="skill-label">{skill}</a>'

    @env.macro
    def list_unique_labels(lower_limit=1, upper_limit=None, star_threshold=None, small_star_threshold=None):
        """
        Generate a list of all unique skill labels, filtered by occurrence count.

        Args:
            lower_limit (int): Minimum number of occurrences to include a skill.
            upper_limit (int or None): Maximum number of occurrences to include a skill.
            star_threshold (int or None): Add a large star icon if the skill occurs more than this number.
            small_star_threshold (int or None): Add a small star icon if the skill occurs more than this number but less than star_threshold.
        """
        # Access the global Counter of skill occurrences
        skill_counts = env.variables['skill_counts']
        # Filter skills based on the limits
        filtered_skills = {
            skill: count
            for skill, count in skill_counts.items()
            if count >= lower_limit and (upper_limit is None or count <= upper_limit)
        }
        # Sort skills by frequency (descending) and alphabetically for ties
        sorted_skills = sorted(filtered_skills.items(), key=lambda x: (-x[1], x[0]))
        # Render each skill as a clickable label, optionally adding a star
        return (
            '<div class="label-container">'
            + "".join(
                f'<a href="?q={skill}" class="skill-label">{skill}'
                + (
                    " <i class='fa-solid fa-star'></i>"  # Large star
                    if star_threshold and count > star_threshold
                    else (
                        " <i class='fa-regular fa-star'></i>"  # Small star
                        if small_star_threshold and count > small_star_threshold
                        else ""
                    )
                )
                + "</a>"
                for skill, count in sorted_skills
            )
            + "</div>"
        )

    
    @env.macro
    def custom_button(text, url, color="teal"):
        """
        Generate a styled button with customizable color and hover effects.

        Args:
            text (str): The text to display on the button.
            url (str): The URL the button links to.
            color (str): The color of the button. Options: "teal", "gray".

        Returns:
            str: HTML string for the button.
        """
        # Define button styles
        colors = {
            "teal": {
                "background": "#27788b",
                "hover": "#3596aa",
                "text": "white",
            },
            "gray": {
                "background": "#555555",
                "hover": "#777777",
                "text": "white",
            },
        }

        # Get the styles for the selected color
        style = colors.get(color, colors["teal"])  # Default to teal if color is invalid

        # Generate the HTML for the button using an f-string
        return f"""
<a href="{url}">
    <button style="
        background-color: {style['background']};
        color: {style['text']};
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        width: 100%;
        cursor: pointer;
        border: none;
        transition: background-color 0.3s ease;
    " onmouseover="this.style.backgroundColor='{style['hover']}'" onmouseout="this.style.backgroundColor='{style['background']}'">
        {text}
    </button>
</a>
"""