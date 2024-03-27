
# Requirements 
# pip install llama-index-llms-openai
# pip install llama-parse
# pip install llama-index-agent-openai
# pip install llama-index-core


# Import relevant classes from correct modules 
import requests
import streamlit as st
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.tools import FunctionTool
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
import os

# Set environmental variables
os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxOZ7M"
openai_api_key = os.environ["OPENAI_API_KEY"]

# Define Function 1 for Moosa API Call 

def fetch_freight_rates(origin, destination, cargo_weight, cargo_type, weight, length, width, height, units):
    url = "http:xxxxxxxxxxxxxxxxxxxxxe"
    params = {
        "origin": origin,
        "destination": destination,
        "cargoWeight": cargo_weight,
        "cargoType": cargo_type,
        "weight": weight,
        "length": length,
        "width": width,
        "height": height,
        "units": units
    }
    response = requests.get(url, params=params)

    if response.ok:
        data = response.json()
        
        relevant_shipments = [
            quote for quote in data
            ]

        if relevant_shipments:
            print("Freight rates quote:")
            shipments_details = []
            for shipment in relevant_shipments:
                shipment_dict = {
                    "quoteId": shipment["quoteId"],
                    "countryOfOrigin": shipment["countryOfOrigin"],
                    "portOfOrigin": shipment["portOfOrigin"],
                    "portOfOriginCode": shipment["portOfOriginCode"],
                    "countryOfDestination": shipment["countryOfDestination"],
                    "portOfDestination": shipment["portOfDestination"],
                    "portOfDestinationCode": shipment["portOfDestinationCode"],
                    "carrier": shipment["carrier"],
                    "rate": shipment["generalCargo"] if shipment["generalCargo"] else shipment["hazardousCargo"],
                    "validFrom": shipment["validFrom"],
                    "validTo": shipment["validTo"],
                    "terms": shipment["terms"],
                    "bookingLink": shipment["bookingLink"]
                }
                shipments_details.append(shipment_dict)
            return shipments_details
        else:
            print("No relevant shipments found.")
    else:
        print(f"Error fetching data. Status code: {response.status_code}")

# Define a placeholder Function 2 for multiplication (Can be reporposed for Air or RoRo freights later)

def multiply(a: int, b: int) -> int:
    return a * b

# Define Function 3 for a RAG that chats with relevant company documents

def get_rag_response(query):
    parser = LlamaParse(
        api_key="llx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxlbGh7",
        result_type="text",
        language="en",
        varbose=True
    )

    documents = parser.load_data("C:\\Users\\user\\Documents\\Jan 2024\\Projects\\RAGs\\Files\\VehicleImport.pdf")

    index = VectorStoreIndex.from_documents(documents)
    print("Index created")

    index.set_index_id("vector_index")
    index.storage_context.persist("./storage")
    print("Saved index to disk")

    storage_context = StorageContext.from_defaults(persist_dir="storage")
    print("Rebuilt storage context")

    index = load_index_from_storage(storage_context, index_id="vector_index")
    print("Loaded index")

    query_engine = index.as_query_engine(response_mode="tree_summarize")
    response = query_engine.query("What is the age restriction for car that can be imported into Kenya?")
    print("Returning response")
    return response

# Set up tools for the 3 Functions 
freight_rates_tool = FunctionTool.from_defaults(fn=fetch_freight_rates)
multiply_tool = FunctionTool.from_defaults(fn=multiply)
rag_tool = FunctionTool.from_defaults(fn=get_rag_response)

# Set up a single agent and give it multiple functions to call depending on user query
openai_key ="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxOZ7M"
llm = OpenAI(api_key=openai_key, model = "gpt-3.5-turbo")
agent = OpenAIAgent.from_tools([rag_tool, freight_rates_tool, multiply_tool], llm=llm, verbose=True)

# Streamlit app setup
st.title("Freight rates app")
user_query = st.text_input("Ask for our rates here:")

if user_query:
    response = agent.chat(user_query)
    st.subheader("Rates: ")
    st.write(response)






