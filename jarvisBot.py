import pyttsx3
import wikipedia as wp
import speech_recognition as sr
import time

vconfig = pyttsx3.init()
stt = sr.Recognizer()
vconfig.setProperty("rate", 188)


def qa(audio_source):
    try:
        searchQuery = stt.recognize_google(audio_source)
        print("\n" + searchQuery)
        wiki = wp.summary(searchQuery, sentences=1)
        print("\n" + wiki)
        vconfig.say(wiki)
        print("\nWould you like to hear more?")
        vconfig.say("Would you like to hear more?")
        vconfig.runAndWait()
        with sr.Microphone() as explain_source:
            explain = stt.listen(explain_source)
            explainyn = stt.recognize_google(explain)
        print("\n" + explainyn)
        if explainyn == "yes":
            wikisum = wp.summary(searchQuery)
            print("\n" + wikisum)
            vconfig.say(wikisum)
            vconfig.runAndWait()
        elif explainyn == "no":
            pass
        else:
            print("\nSorry, I didn't recognize what you were trying to say.")
            vconfig.say("Sorry, I didn't recognize what you were trying to say.")
            vconfig.runAndWait()
    except Exception:
        print("\nApologies, the query could not be searched.")
        vconfig.say("Apologies, the query could not be searched.")
        vconfig.runAndWait()


if __name__ == "__main__":
    with sr.Microphone() as source:
        time.sleep(0.5)
        print("\nRussl, at your assistance, ask anything.")
        vconfig.say("Russl, at your assistance, ask anything.")
        vconfig.runAndWait()
        audio = stt.listen(source)
        qa(audio)
