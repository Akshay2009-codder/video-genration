# 🎬 Automated Video Creation Pipeline

## 📌 Overview

This project implements a fully automated video generation pipeline using Python.  
The system automatically selects a topic, generates a short script, converts the script into speech, and creates a final video by combining audio with a background image.

The entire process runs without manual intervention.

---

## 🚀 Features

- ✅ Automatic topic selection
- ✅ AI-based script generation
- ✅ Text-to-Speech conversion (MP3 output)
- ✅ Automatic video creation (MP4 output)
- ✅ Modular and scalable architecture
- ✅ Fully automated execution

---

## 🛠️ Tech Stack

- Python 3.x
- OpenAI API (for script generation)
- gTTS (Google Text-to-Speech)
- MoviePy (Video creation)

---

## 📂 Project Structure

```
video-automation/
│
├── main.py
├── topic_generator.py
├── script_generator.py
├── voice_generator.py
├── video_creator.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works (Pipeline Flow)

1. **Topic Selection**  
   A topic is randomly selected from a predefined list.

2. **Script Generation**  
   The topic is sent to the OpenAI API to generate a short engaging script.

3. **Text-to-Speech Conversion**  
   The generated script is converted into an MP3 voice file using gTTS.

4. **Video Creation**  
   The audio file is combined with a background image using MoviePy to generate the final video.

---

## ▶️ How to Run

### 1️⃣ Clone the Repository

```
git clone <your-repo-link>
cd video-automation
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Set OpenAI API Key (Windows PowerShell)

```
setx OPENAI_API_KEY "your_api_key_here"
```

Restart terminal after setting the key.

### 4️⃣ Run the Pipeline

```
python main.py
```

---

## 📤 Output Files

After execution, the following files will be generated:

- `script.txt` → Generated script  
- `voice.mp3` → Text-to-speech audio  
- `final_video.mp4` → Final generated video  

---

## 🔮 Future Improvements

- Dynamic AI image generation
- Automated thumbnail creation
- Integration with n8n workflow automation
- Automatic upload to YouTube/Instagram
- Enhanced 3D-style visuals

---

## 📌 Notes

This project demonstrates:

- Modular coding practices
- Automation design thinking
- API integration
- Media processing using Python

---

## 👤 Author
Akshay 
Python & Automation Enthusiast
