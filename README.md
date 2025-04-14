# Audio_Analysis


# **Speech Analysis Pipeline - Process Flow**

```text
                            ┌───────────────────────────────┐
                            │  Input Audio File (.wav/.mp3) │
                            └───────────────────────────────┘
                                        │
                                        ▼
                ┌────────────────────────────────────────────────────────┐
                │ Audio Preprocessing                                    │
                │ - Load audio using pydub                               │
                │ - Convert to mono channel (1-channel)                  │
                │ - Resample to 16kHz frame rate                         │
                │ - Export to in-memory buffer (.wav format)             │
                └────────────────────────────────────────────────────────┘
                                        │
                                        ▼
                ┌────────────────────────────────────────────────────────┐
                │ Speech Recognition (VOSK KaldiRecognizer)              │
                │ - Load VOSK model                                      │
                │ - Transcribe audio in chunks                           │
                │ - Extract recognized words with timestamps             │
                │ - Generate full transcript                             │
                └────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│                               Analyze Speech Features                                         │
│                                                                                               │
│ ▸ Pauses: Identify gaps > 0.5s between words                                                  │
│ ▸ Hesitations: Detect filler words like “um”, “like”, “so”, etc. (regex match)                │
│ ▸ Repetitions: Find repeated bigrams (e.g., “you know”, “I mean”)                             │
│ ▸ Speech Rate: Calculate number of words per second                                           │
│ ▸ Pitch Variability: Use Librosa to extract pitch and measure std deviation                   │
│ ▸ Lost Words: Sentences with < 5 words using spaCy                                            │
│ ▸ Incomplete Sentences: Sentences not ending with valid syntax (e.g., no ROOT or punctuation) │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
                ┌────────────────────────────────────────────────────────┐
                │ Output Metrics                                         │
                │ - Final Transcript                                     │
                │ - Pauses list                                          │
                │ - Hesitation words                                     │
                │ - Repeated phrases                                     │
                │ - Speech rate                                          │
                │ - Pitch variability                                    │
                │ - Lost/Incoherent sentences                            │
                └────────────────────────────────────────────────────────┘

