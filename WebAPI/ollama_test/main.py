from langchain_ollama import ChatOllama
import streamlit as st
import time

if "time_record" not in st.session_state:
    st.session_state.time_record = []

# Model
models = {
    "Qwen3.8": "qwen3.8-flash-next:125b-mlx",
    "Qwen3.6": "qwen3.6:latest",
    "Phi4Q4": "phi4:14b-q4_K_M",
    "Phi4Q8": "phi4:14b-q8_0"
}

selected_model = st.selectbox(
                "Select a model?",
                ("Qwen3.8","Qwen3.6","Phi4Q4","Phi4Q8"),
                index = None                
)


if selected_model:
    # Target IP: 172.29.190.0
    llm = ChatOllama(
        base_url="http://172.29.190.0:11434",
        model= models[selected_model],
        temperature=0.1,
        num_predict=128
        )

    prompt = st.text_input("Ask something?")
    if st.button("Ask"):
        response = ""
        if prompt:
            # Test execution
            start_time = time.perf_counter()
            try:
               
                response = llm.invoke(prompt)
                output = response.content
                st.markdown(output)
            except Exception as httperror:
                output = f"Error: {httperror}"
                st.markdown(output)

            st.session_state.time_record.append(
                {
                    "Model": selected_model,
                    "Prompt": prompt,
                    "Time": time.perf_counter() - start_time
                 }
            )
            st.write(st.session_state.time_record)

