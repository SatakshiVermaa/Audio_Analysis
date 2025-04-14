# **Speech Analysis Pipeline - Process Flow**

![image](https://github.com/user-attachments/assets/08971802-c0d0-4638-84b0-f3e446a911e8)

# **Work Includes**

1. The below code uses the Vosk speech recognition model to convert the audio into text. Additionally, it captures the precise timing of each word's occurrence, which is very useful for verifying pauses and how fast someone is talking.

2. Feature Analysis: The extracted text column namely `transcript` was examined to determine many speech-related features:
   - **Pauses**: Detects prolonged pauses between words (more than 0.5 seconds), which can reflect a person thinking or stalling.
   - **Hesitation Markers**: Detects frequent filler words such as "um," "ah," "like," "you know," "well," "I mean," and "actually."

           - Filler Sounds: These are the basic sounds used to fill pauses, like "um," "uh," "ah," "er," and "hmm".
           - Filler Phrases: These are short phrases used to give the speaker time to think or soften a statement, such as "you know," "I mean," "well," and "actually."
           - Discourse Markers: These are words that help connect ideas and guide the listener, but can also be used as fillers, like "so," "basically," and "really".
     
   - **Word Repetitions**: Identifies repeating word pairs, which may be an indication of difficulty remembering words or overstressing a point.
   - **Speech Rate**: Determines the number of words spoken in a single second.
   - **Pitch Variability**: Examines the variation of loudness that can be shown through emotion or emphasis.
   - **Incomplete Sentences**: Totals sentences which are extremely brief (fewer than 3 words), and possibly indicate incomplete thoughts.
   - **Lost or Forgotten Words**: Flags very short or truncated sentences that may indicate difficulty with word choice.



