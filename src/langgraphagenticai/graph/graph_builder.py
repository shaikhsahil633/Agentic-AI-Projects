from langgraph.graph import START,END,MessagesState,StateGraph
from langgraph.prebuilt import tools_condition,ToolNode
from langchain_core.prompts import ChatMessagePromptTemplate
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatNode

class GraphBuilder:

    def __init__(self,model): 
        self.llm= model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Build a basic chatbot graph using LangGraph.
        This method initialize a chatbot node using 'BasicChatbotNode' class
        and integrates it into the graph.The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        self.basic_chatbot_node = BasicChatNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
    
    def setup_graph(self,usecase:str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        return self.graph_builder.compile()