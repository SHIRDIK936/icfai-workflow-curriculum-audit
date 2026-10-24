from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ICFAI Workflow & Curriculum Audit",
    page_icon="🎓",
    layout="wide",
)

ROOT = Path(__file__).resolve().parent.parent
TASK1 = ROOT / "Task-1-College-Workflow"
TASK2 = ROOT / "Task-2-Curriculum-Redesign"

st.title("🎓 ICFAI Workflow & Curriculum Audit")
st.caption(
    "Academic assignment | B.Tech Artificial Intelligence & "
    "Machine Learning | 2023–2027"
)

st.warning(
    "This is an academic prototype. Task 1 uses a hypothetical "
    "workflow and synthetic tests. Curriculum changes are proposals, "
    "not approved institutional changes."
)


@st.cache_data
def load_csv(path):
    return pd.read_csv(path)


page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Official Curriculum",
        "Proposed Redesign",
        "Workflow Tests",
        "Limitations",
    ],
)

if page == "Overview":
    st.header("Project Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Assignments", "2")
    col2.metric("Workflow Test Scenarios", "5")
    col3.metric("AI Exercise Reference Tests", "5")

    st.subheader("Task 1")
    st.write(
        "Investigates a hypothetical college laboratory booking "
        "and approval workflow, including exceptions, synthetic "
        "testing, and estimated time savings."
    )

    st.subheader("Task 2")
    st.write(
        "Reviews the AI/ML curriculum and proposes updates based "
        "on practical skills, industry job descriptions, and "
        "AI-assisted learning exercises."
    )

elif page == "Official Curriculum":
    st.header("Official Curriculum Transcription")

    path = TASK2 / "official_curriculum.csv"

    if path.exists():
        df = load_csv(path)

        st.dataframe(df, use_container_width=True)

        if {"Semester", "Credits"}.issubset(df.columns):
            numeric_credits = pd.to_numeric(
                df["Credits"], errors="coerce"
            )

            totals = (
                df.assign(Numeric_Credits=numeric_credits)
                .groupby("Semester", as_index=False)["Numeric_Credits"]
                .sum()
            )

            st.subheader("Recorded Numeric Credits by Semester")
            st.bar_chart(
                totals.set_index("Semester")["Numeric_Credits"]
            )

            st.info(
                "Semesters VII and VIII contain unallocated credit "
                "entries. Their chart values must not be interpreted "
                "as official zero-credit semesters."
            )

            st.metric(
                "Recorded Numeric Credits",
                f"{numeric_credits.sum():g}",
            )
    else:
        st.error("official_curriculum.csv was not found.")

elif page == "Proposed Redesign":
    st.header("Proposed Curriculum Changes")

    path = TASK2 / "proposed_curriculum.csv"

    if path.exists():
        df = load_csv(path)

        st.dataframe(df, use_container_width=True)

        if "Action" in df.columns:
            st.subheader("Recommendations by Category")

            counts = df["Action"].value_counts()
            st.bar_chart(counts)

            actions = st.multiselect(
                "Filter recommendations",
                sorted(df["Action"].dropna().unique()),
                default=sorted(df["Action"].dropna().unique()),
            )

            st.dataframe(
                df[df["Action"].isin(actions)],
                use_container_width=True,
            )

        if {
            "Current_Credits",
            "Proposed_Credits",
        }.issubset(df.columns):
            current = pd.to_numeric(
                df["Current_Credits"], errors="coerce"
            ).sum()

            proposed = pd.to_numeric(
                df["Proposed_Credits"], errors="coerce"
            ).sum()

            col1, col2, col3 = st.columns(3)
            col1.metric("Listed Current Credits", f"{current:g}")
            col2.metric("Listed Proposed Credits", f"{proposed:g}")
            col3.metric("Net Change in Listed Rows", f"{proposed-current:+g}")

            st.caption(
                "This CSV is a change register, not the complete "
                "programme curriculum. These totals apply only "
                "to listed rows."
            )
    else:
        st.error("proposed_curriculum.csv was not found.")

elif page == "Workflow Tests":
    st.header("Task 1 — Synthetic Workflow Tests")

    path = TASK1 / "test_cases.csv"

    if path.exists():
        df = load_csv(path)
        st.dataframe(df, use_container_width=True)
    else:
        st.error("test_cases.csv was not found.")

    st.info(
        "The five scenarios are normal request, missing information, "
        "duplicate booking, unauthorized approval, and failed step. "
        "See the repository test script for executable checks."
    )

elif page == "Limitations":
    st.header("Evidence and Limitations")

    st.markdown(
        """
        - Task 1 is a hypothetical process model, not a verified
          observation of an ICFAI workflow.
        - All workflow tests use synthetic data.
        - Time savings are estimates, not measured institutional outcomes.
        - The curriculum transcription contains unresolved credit
          discrepancies.
        - The proposed redesign has not been approved by faculty.
        - The five AI exercise scripts test reference answers, not
          actual AI-generated responses.
        - Job-description evidence reflects selected postings and
          does not represent every employer.
        """
    )

st.divider()
st.caption("Academic prototype | Prepared October 2026")