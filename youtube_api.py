import speech_recognition as sr
import pywhatkit

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("何の曲を再生しますか？")
        audio = recognizer.listen(source)

    try:
        # 音声認識を実行し、変数に格納する
        recognized_text = recognizer.recognize_google(audio, language='ja-JP')

        print("認識結果:", recognized_text)

        # 認識した音声を使用してYouTubeで曲を再生
        if recognized_text:
            print("曲を再生中...")
            pywhatkit.playonyt(recognized_text)

    except sr.UnknownValueError:
        print("音声を認識できませんでした。")
    except sr.RequestError as e:
        print(f"Google Web Speech APIにアクセスできませんでした: {e}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
