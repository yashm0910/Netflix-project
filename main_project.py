import streamlit as st
import pandas as pd

st.title("🎬 Netflix Content Analysis Dashboard")

st.header("1. Dataset Overview")

st.write("""
We began by importing and cleaning the **Netflix dataset** (`updated_netflix.csv`).  
This included:
- Handling missing values
- Splitting duration into numerical + type (e.g., '90 min', '1 Season')
- Converting string dates into datetime objects
- Creating derived columns for analysis like: `release_year`, `month_added`, `day_of_week`, etc.

Once cleaned, the dataset was imported into **MySQL** for SQL-based querying and analysis.
""")

st.header("2. Movie vs. TV Show Breakdown")

st.image("movies_vs_tvshow_plot.jpg")

st.markdown("**SQL Query:**")
st.image("movies_vs_tvshow_sql.jpg")

st.write("""
- **Explanation:**
  - This helps understand the overall makeup of Netflix’s catalog.
  - It sets the base for further analysis like duration and genre.
  - We analyze both movies and shows separately later.

- **Conclusion:** Netflix offers more movies than TV shows, though the platform’s investment in long-form series has been rising steadily in recent years.
""")


st.header("3. Titles Released Per Year")

st.markdown("**SQL Query:**")
st.image("titles_release_peryear_sql.jpg")

st.write("""
- **Explanation:**
  - Shows Netflix’s growth phase and content scaling.
  - Spikes reflect the shift toward original content and global expansion.
  - Dips may relate to licensing changes or global events (e.g., 2020 pandemic).

- **Conclusion:** A surge in releases began after 2015, peaking in 2019–2020, reflecting Netflix’s aggressive global expansion and original content push.
""")

st.header("4. Popular Genres on Netflix")

st.image("genres_classification_plot.jpg")

st.markdown("**SQL Query:**")
st.image("genres_classification_sql.jpg")


st.write("""
- **Explanation:**
  - Genre data helps identify audience targeting.
  - Useful for market research and content recommendation models.
  - Some content appears in multiple genres (multi-label).

- **Conclusion:** Drama, Comedies, and Documentaries dominate the platform, appealing to a wide range of global audiences.
""")

st.header("5. Most Active Directors on Netflix")

st.image("top_directors_plot.jpg")

st.markdown("**SQL Query:**")
st.image("top_directors_sql.jpg")

st.write("""
- **Explanation:**
  - Highlights frequent collaborations (where director names are available).
  - Suggests active contributors with high volume, useful for trend or quality analysis.
  - However, many entries have **missing or 'Unknown' directors**, likely due to incomplete metadata.

- **Conclusion:** While some well-known directors appear in the top list, a large portion of content is tagged with unknown or missing director names.  
  Dropping the `director` column would lead to loss of meaningful insights where data **is** present — so we kept it, used filters, and extracted value where possible.
""")

st.header("6. Release Pattern by Month")

st.image("monthly_release_plot.jpg")

st.markdown("**SQL Query:**")
st.image("monthly_release_sql.jpg")


st.write("""
- **Explanation:**
  - Helps spot seasonal content drops (e.g., holidays, festivals).
  - Q4 peaks show marketing strategy around year-end viewership.
  - Can guide decisions for optimal release timing.

- **Conclusion:** October and December show release peaks, likely tied to festive or holiday season viewership spikes.
""")

st.header("7. Day of the Week Release Pattern")

st.image("weekday_release_plot.jpg")

st.markdown("**SQL Query:**")
st.image("weekday_release_sql.jpg")


st.write("""
- **Explanation:**
  - Shows Netflix’s weekly release strategy.
  - Most new content is scheduled before weekends for higher engagement.
  - Business insight: viewers binge over weekends.

- **Conclusion:** Most releases are concentrated from **Thursday to Saturday**, strategically timed for weekend viewers.
""")

st.header("8. Movie Duration Distribution")

st.image("duration_plot.jpg")

st.markdown("**SQL Query:**")
st.image("duration_sql.jpg")


st.write("""
- **Explanation:**
  - Validates standard duration trends in film production.
  - Helps platforms understand what durations users prefer.
  - Supports auto-skipping algorithms or recommendations.

- **Conclusion:** Most Netflix movies fall within the 80–120 minute range, matching standard feature-length expectations.
""")

st.header("9. TV Shows: Season Count")

st.image("movie_season_plot.jpg")

st.write("""
- **Explanation:**
  - Many shows have only 1 season—possibly new launches, test pilots, or mini-series.
  - Multi-season shows indicate long-term audience interest.
  - Business strategy: single-season = lower cost risk.

- **Conclusion:** A large portion of shows have **only 1 season**, possibly indicating mini-series, limited series, or newly launched content.
""")

st.subheader("📌 Summary & Learnings")

st.write("""
- Netflix's content library is heavily **movie-dominant**, but multi-season series are growing.
- **2017–2020** saw explosive release growth, driven by original programming.
- **Drama**, **Comedy**, and **Documentary** remain leading genres.
- **Friday–Saturday** and **October–December** are peak release windows, aligned with audience demand.
- Most content follows common patterns (90 min movies, single-season series), showing Netflix’s structured approach to content length.

This project demonstrates:
- SQL querying  
- Python visualization  
- Data storytelling  
- Real-world dashboarding via Streamlit
""")
