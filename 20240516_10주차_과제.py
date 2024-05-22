{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOc+4hekq/mZ3PAeRESpq/D"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "683USZPXO6UT"
      },
      "outputs": [],
      "source": [
        "from datetime import datetime\n",
        "\n",
        "place=input(\"경기가 열린 곳은? \")\n",
        "time=input(\"경기가 열린 시간은? \")\n",
        "opponent=input(\"상대 팀은? \")\n",
        "goals=input(\"손흥민은 몇 골을 넣었나요? \")\n",
        "aids=input(\"도움은 몇 개인가요? \")\n",
        "score_me=input(\"손흥민 팀이 넣은 골 수는?\" )\n",
        "score_you=input(\"상대 팀이 넣은 골 수는? \")\n",
        "\n",
        "news=\"[프리미어 리그 속보(\"+str(datetime.now())+\")]\\n\"\n",
        "news=news+\"손흥민 선수는 \"+place+\"에서 \"+time+\"에 열린 경기에 출전하였습니다. \"\n",
        "news=news+\"상대 팀은 \"+opponent+\"입니다. \"\n",
        "\n",
        "if score_me>score_you:\n",
        "  news=news+\"손흥민 선수의 팀이 \"+score_me+\"골을 넣어 \"+score_you+\"골을 넣은 상대 팀을 이겼습니다. \"\n",
        "elif score_me<score_you:\n",
        "  news=news+\"손흥민 선수의 팀이 \"+score_me+\"골을 넣어 \"+score_you+\"골을 넣은 상대 팀에게 졌습니다. \"\n",
        "else:\n",
        "  news=news+\"두 팀은 \"+score_me+\"대\"+score_you+\"로 비겼습니다. \"\n",
        "\n",
        "\n",
        "if int(goals)>0 and int(aids)>0:\n",
        "  news=news+\"손흥민 선수는 \"+goals+\"골에 도움 \"+aids+\"개로 승리를 크게 이끌었습니다. \"\n",
        "elif int(goals)>0 and int(aids)==0:\n",
        "  news=news+\"손흥민 선수는 \"+goals+\"골로 승리를 크게 이끌었습니다. \"\n",
        "elif int(goals)==0 and int(aids)>0:\n",
        "  news=news+\"손흥민 선수는 골은 없지만 도움 \"+aids+\"개로 승리하는 데 공헌하였습니다. \"\n",
        "else:\n",
        "  news=news+\"아쉽게도 이번 경기에서 손흥민의 발끝은 침묵을 지켰습니다. \"\n",
        "\n",
        "print(news)\n",
        "\n",
        "from gtts import gTTS\n",
        "import playsound\n",
        "\n",
        "tts=gTTS(text=news, lang='ko')\n",
        "tts.save(\"news_Son.mp3\")\n",
        "playsound.playsoung(\"news_son.mp3\",True)"
      ]
    }
  ]
}