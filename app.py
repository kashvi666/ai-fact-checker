import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.claim_extractor import extract_claims
from utils.fact_verifier import verify_claim

st.set_page_config(
    page_title="AI Fact Checker",
    layout="wide"
)

st.title("kAI Fact Checker")
st.write("Upload a PDF to extract and verify factual claims using live web data.")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    # Step 1: Read PDF
    with st.spinner("📄 Reading PDF..."):
        try:
            text = extract_text_from_pdf(uploaded_file)
        except Exception as e:
            st.error("Failed to read PDF")
            st.code(str(e))
            st.stop()

    # Step 2: Extract claims
    with st.spinner("🔍 Extracting factual claims..."):
        try:
            claims = extract_claims(text)
        except Exception as e:
            st.error("Failed to extract claims from the document")
            st.code(str(e))
            st.stop()

    # Display extracted claims
    st.subheader("📌 Extracted Claims")
    for idx, c in enumerate(claims, start=1):
        st.write(f"{idx}. {c.get('claim', 'Invalid claim')}")

    st.divider()

    # Step 3: Verify claims
    st.subheader("✅ Verification Results")

    for c in claims:
        claim_text = c.get("claim")

        if not claim_text:
            continue

        with st.spinner(f"Checking: {claim_text}"):
            result = verify_claim(claim_text)

        st.markdown(f"**Claim:** {claim_text}")
        st.markdown(result)
        st.divider()
