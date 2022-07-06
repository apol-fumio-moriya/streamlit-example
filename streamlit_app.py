import streamlit as st

st.set_page_config(
    page_title="ilodoli タイプ判断", page_icon="📊", initial_sidebar_state="expanded"
)

st.write(
    """
# ilodoli タイプ診断
ilodoli にてあなたのタイプを診断してみませんか。
"""
)

decide1 = st.radio(
    f"自分の考えに夢中になって、周囲のことを無視したり忘れることがよくある。",
    options=["Yes", "No"],
    )
decide2 = st.radio(
    f"受信箱がごちゃごちゃするのが我慢できず、できるだけ早くEメールに返答しようとする。",
    options=["Yes", "No"],
    )
decide3 = st.radio(
    f"プレッシャーがあるときでも常にリラックスし、集中できる。",
    options=["Yes", "No"],
    )
decide4 = st.radio(
    f"通常、自分から話を始めることはない。",
    options=["Yes", "No"],
    )

with st.form(key='my_form'):
    submit_button = st.form_submit_button(label="次へ")

'''
uploaded_file = st.file_uploader("Upload CSV", type=".csv")

use_example_file = st.checkbox(
    "Use example file", False, help="Use in-built example file to demo the app"
)

ab_default = None
result_default = None

# If CSV is not uploaded and checkbox is filled, use values from the example file
# and pass them down to the next if block
if use_example_file:
    uploaded_file = "Website_Results.csv"
    ab_default = ["variant"]
    result_default = ["converted"]

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.markdown("### Data preview")
    st.dataframe(df.head())

    st.markdown("### Select columns for analysis")
    with st.form(key="my_form"):
        ab = st.multiselect(
            "A/B column",
            options=df.columns,
            help="Select which column refers to your A/B testing labels.",
            default=ab_default,
        )
        if ab:
            control = df[ab[0]].unique()[0]
            treatment = df[ab[0]].unique()[1]
            decide = st.radio(
                f"Is *{treatment}* Group B?",
                options=["Yes", "No"],
                help="Select yes if this is group B (or the treatment group) from your test.",
            )
            if decide == "No":
                control, treatment = treatment, control
            visitors_a = df[ab[0]].value_counts()[control]
            visitors_b = df[ab[0]].value_counts()[treatment]

        result = st.multiselect(
            "Result column",
            options=df.columns,
            help="Select which column shows the result of the test.",
            default=result_default,
        )

        if result:
            conversions_a = (
                df[[ab[0], result[0]]].groupby(ab[0]).agg("sum")[result[0]][control]
            )
            conversions_b = (
                df[[ab[0], result[0]]].groupby(ab[0]).agg("sum")[result[0]][treatment]
            )

        with st.expander("Adjust test parameters"):
            st.markdown("### Parameters")
            st.radio(
                "Hypothesis type",
                options=["One-sided", "Two-sided"],
                index=0,
                key="hypothesis",
                help="TBD",
            )
            st.slider(
                "Significance level (α)",
                min_value=0.01,
                max_value=0.10,
                value=0.05,
                step=0.01,
                key="alpha",
                help=" The probability of mistakenly rejecting the null hypothesis, if the null hypothesis is true. This is also called false positive and type I error. ",
            )

        submit_button = st.form_submit_button(label="Submit")

    if not ab or not result:
        st.warning("Please select both an **A/B column** and a **Result column**.")
        st.stop()

    # type(uploaded_file) == str, means the example file was used
    name = (
        "Website_Results.csv" if isinstance(uploaded_file, str) else uploaded_file.name
    )
    st.write("")
    st.write("## Results for A/B test from ", name)
    st.write("")

    # Obtain the metrics to display
    calculate_significance(
        conversions_a,
        conversions_b,
        visitors_a,
        visitors_b,
        st.session_state.hypothesis,
        st.session_state.alpha,
    )

    mcol1, mcol2 = st.columns(2)

    # Use st.metric to diplay difference in conversion rates
    with mcol1:
        st.metric(
            "Delta",
            value=f"{(st.session_state.crb - st.session_state.cra):.3g}%",
            delta=f"{(st.session_state.crb - st.session_state.cra):.3g}%",
        )
    # Display whether or not A/B test result is statistically significant
    with mcol2:
        st.metric("Significant?", value=st.session_state.significant)

    # Create a single-row, two-column DataFrame to use in bar chart
    results_df = pd.DataFrame(
        {
            "Group": ["Control", "Treatment"],
            "Conversion": [st.session_state.cra, st.session_state.crb],
        }
    )
    st.write("")
    st.write("")

    # Plot bar chart of conversion rates
    plot_chart(results_df)

    ncol1, ncol2 = st.columns([2, 1])

    table = pd.DataFrame(
        {
            "Converted": [conversions_a, conversions_b],
            "Total": [visitors_a, visitors_b],
            "% Converted": [st.session_state.cra, st.session_state.crb],
        },
        index=pd.Index(["Control", "Treatment"]),
    )

    # Format "% Converted" column values to 3 decimal places
    table1 = ncol1.write(table.style.format(formatter={("% Converted"): "{:.3g}%"}))

    metrics = pd.DataFrame(
        {
            "p-value": [st.session_state.p],
            "z-score": [st.session_state.z],
            "uplift": [st.session_state.uplift],
        },
        index=pd.Index(["Metrics"]),
    )

    # Color negative values red; color significant p-value green and not significant red
    table2 = ncol1.write(
        metrics.style.format(
            formatter={("p-value", "z-score"): "{:.3g}", ("uplift"): "{:.3g}%"}
        )
        .applymap(style_negative, props="color:red;")
        .apply(style_p_value, props="color:red;", axis=1, subset=["p-value"])
    )
'''
