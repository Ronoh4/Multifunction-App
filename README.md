**Freight Rates App with Multi-function Agent**
This code provides a Streamlit application that allows users to interact with various functionalities through a single interface.

**Functionalities:**

Fetch Freight Rates: Calculates freight rates for cargo shipments based on origin, destination, and cargo details. (Uses external Moosa API)
Multiplication: Performs basic multiplication of two numbers. (Placeholder, can be replaced with other calculations)
Document Retrieval with Answer Generation (RAG): Answers user questions based on a specific document ("VehicleImport.pdf"). (Uses LlamaParse library)

**Requirements:**

llama-index-llms-openai
llama-parse
llama-index-agent-openai
llama-index-core
Instructions:

Replace the placeholder values for OPENAI_API_KEY and llx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxlbGh7 with your actual API keys.
Ensure the path to your document ("C:\Users\user\Documents\Jan 2024\Projects\RAGs\Files\VehicleImport.pdf") is correct.
Run the script.

**Streamlit App:**

The app displays a title "Freight Rates App" and a text input field for users to enter their queries. Upon submitting a query, the app utilizes the OpenAIAgent to determine the most appropriate function to call based on the user's intent. It then retrieves the response and displays it under the "Rates" section.

**Additional Notes:**

The multiply function is a placeholder and can be replaced with other calculations.
The RAG functionality demonstrates how to use LlamaParse to answer questions from a specific document.

**Further Enhancements:**

Expand the functionality set beyond the provided examples.
Implement error handling for potential issues with external APIs or document retrieval.
Enhance the user interface for a more interactive experience.
