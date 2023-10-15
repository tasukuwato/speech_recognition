import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def main():
    recognizer = sr.Recognizer()

    # Spotify APIの認証情報
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', redirect_uri='YOUR_REDIRECT_URI', scope='user-library-read user-read-playback-state user-modify-playback-state'))

    with sr.Microphone() as source:
        print("何の曲を再生しますか？")
        audio = recognizer.listen(source)

    try:
        # 音声認識を実行し、変数に格納する
        recognized_text = recognizer.recognize_google(audio, language='ja-JP')

        print("認識結果:", recognized_text)

        # 認識した音声を使用してSpotifyで曲を再生
        if recognized_text:
            results = sp.search(q=recognized_text, type='track', limit=1)
            if results and results['tracks']['items']:
                track_uri = results['tracks']['items'][0]['uri']
                sp.start_playback(uris=[track_uri])
                print(f"曲を再生中: {recognized_text}")
            else:
                print(f"曲が見つかりません: {recognized_text}")

    except sr.UnknownValueError:
        print("音声を認識できませんでした。")
    except sr.RequestError as e:
        print(f"Google Web Speech APIにアクセスできませんでした: {e}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
