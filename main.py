import streamlit as st
import chess
import chess.svg
import os
import importlib


if __name__ == '__main__':
    #Pasting the name of given IA from agents
    agents=[]
    for root, dirs, files in os.walk("agents"):
        for file in files:
            ai_name=file.replace(".py", "")
            agents.append(ai_name)
            agents.insert(0,"None")
            
    st.title('AI Chess App') #UI Title with st
    #Creating the sidebar's selectbox with agents' list names options
    white_name=st.sidebar.selectbox('Slect the white AI', agents)
    black_name=st.sidebar.selectbox('Slect the black AI', agents)
    #Creating the sidebar button "Play"
    
    if white_name!="None"and black_name!="None":
        st.header(f"{white_name}White versus {black_name}Black")
        st.sidebar.button("Play")
        white_agent=importlib.import_module(f"agents.{white_name}")
        black_agent=importlib.import_module(f"agents.{black_name}")
        board=chess.Board()#board instatciation with chess
        svg_board=chess.svg.board(board)#board as SVG
        with open("svg_board.svg", "w")as svg:
            svg.write(svg_board)
        
    #Legal moves in the board
        legal_moves=list(board.legal_moves)
        st.write(legal_moves)
        


    
