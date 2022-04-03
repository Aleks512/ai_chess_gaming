import streamlit as st
import chess
import chess.svg

if __name__ == '__main__':
    st.title('AI Chess App') #UI Title with st
    board=chess.Board()#board instatciation with chess
    svg_board=chess.svg.board(board)#board as SVG
    with open("svg_board.svg", "w")as svg:
        svg.write(svg_board)
    
