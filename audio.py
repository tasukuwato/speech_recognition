import speech_recognition as sr

def main():
    recognizer = sr.Recognizer()

    # 認識したい単語(正解)を設定する
    target_word = "バナナ"

    with sr.Microphone() as source:
        print("音声入力を待っています...")
        audio = recognizer.listen(source)

    try:
        # 音声認識を実行し、変数に格納する
        recognized_text = recognizer.recognize_google(audio, language='ja-JP')

        print("認識結果:", recognized_text)

        # 認識した音声と正解が一致するか判定
        if target_word in recognized_text:
            print("一致しました！")
        else:
            print("一致しませんでした。")


    # その他エラーに対する出力
    except sr.UnknownValueError:
        print("音声を認識できませんでした。")
    except sr.RequestError as e:
        print(f"Google Web Speech APIにアクセスできませんでした: {e}")

if __name__ == "__main__":
    main()
