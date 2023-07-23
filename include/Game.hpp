#ifndef GAME_HPP
#define GAME_HPP

#include <string>


class Game
{
public:
    Game(const std::string &chessSetDir="ASCII-pieces/set_01");
    ~Game();

    bool Play();

private:
    // Board m_board;

    bool LoadPieces(const std::string &chessSetDir);
};

#endif