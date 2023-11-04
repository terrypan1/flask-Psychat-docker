"""
    聲音轉換助手模塊
    https://platform.openai.com/docs/guides/speech-to-text api範例
"""
import openai
import os
# 設置API密鑰
openai.api_key = "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"
file_path = os.path.join(os.path.dirname(__file__), "..", "..", "static", "uploads", "my_audio.wav")

print(f"檔案路徑：{file_path}")
class VoiceToText:
    @staticmethod
    def voice_to_text():
        # 檢查檔案是否存在
        if os.path.exists(file_path):
            audio_file = open(file_path, "rb")
            
            # 進行語音轉文字操作
            response = openai.Audio.transcribe("whisper-1", audio_file)
            
            try:
                # 嘗試提取文字結果
                text = response["text"]
                print(text)
                return text
            except KeyError:
                print("無效的回應格式：缺少 'text' 鍵")
        else:
            print("my_audio.wav 檔案不存在")

# 使用方法
VoiceToText.voice_to_text()


