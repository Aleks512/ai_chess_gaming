import streamlit as st
import chess
import chess.svg
import os

if __name__ == '__main__':
    #Pasting the name of given IA from agents
    agents=[]
    for root, dirs, files in os.walk("agents"):
        for file in files:
            ai_name=file.replace(".py", "")
            agents.append(ai_name)
            print(agents)
    
    
    st.title('AI Chess App') #UI Title with st
    board=chess.Board()#board instatciation with chess
    svg_board=chess.svg.board(board)#board as SVG
    with open("svg_board.svg", "w")as svg:
        svg.write(svg_board)
        
    #Legal moves in the board
    legal_moves=list(board.legal_moves)
    st.write(legal_moves)
    
