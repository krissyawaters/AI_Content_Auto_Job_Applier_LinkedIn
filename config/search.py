###################################################### LINKEDIN SEARCH PREFERENCES ######################################################

# Search terms focused on your real lane
search_terms = [
    # Core AI enablement / ops
    "AI Community Manager",
    "AI Operations",
    "AI Enablement",
    "AI Program Manager",
    "AI Adoption",

    # RLHF / training / eval
    "AI Trainer",
    "AI Evaluator",
    "AI Content Evaluator",
    "AI Rater",
    "AI Data Trainer",
    "LLM Trainer",
    "AI Quality Rater",
    "Machine Learning Data Specialist",

    # Content + strategy around AI and product
    "Content Strategist",
    "Content Operations",
    "Content Designer",
    "Content Writer",
    "Technical Writer",
    "Digital Strategist"
]

# Remote friendly U.S. targeting
# This is the text that goes into the main LinkedIn search box for location
search_location = "United States"

# Switch to next search term after X applications
switch_number = 12    # a bit tighter rotation so it cycles terms faster

# Randomize search order?
randomize_search_order = False


# >>>>>>>>>>> Job Search Filters <<<<<<<<<<<

# Sort by latest so you are not hitting old junk
sort_by = "Most recent"          # typical LinkedIn label

# Date posted filter to keep things fresh
date_posted = "Past week"       # or "Past week" if you want it even stricter

salary = ""                      # leave blank so it does not filter too hard yet

easy_apply_only = True           # do not waste time on long forms

experience_level = [
    "Entry level",
    "Associate",
    "Mid-Senior level"
]

job_type = ["Full-time", "Contract"]
on_site = ["Remote"]

# Location filter list (used by some scripts separately from search_location)
location = ["United States"]

companies = []
industry = []
job_function = []
job_titles = []
benefits = []
commitments = []

under_10_applicants = False
in_your_network = False
fair_chance_employer = False


## >>>>>>>>>>> RELATED SETTING <<<<<<<<<<<

# First few runs, let it pause after filters so you can see what it is about to do
pause_after_filters = True


## >>>>>>>>>>> SKIP IRRELEVANT JOBS <<<<<<<<<<<

# No company blacklists
about_company_bad_words = []

# No company whitelist logic
about_company_good_words = []

# No bad-word filtering in job descriptions
bad_words = []

# Still required by the bot — but these settings will not skip anything by themselves
security_clearance = False
did_masters = True
current_experience = 5
