import os
import json
import sys
from agents.scout_agent import ScoutAgent
from agents.strategist_agent import StrategistAgent
from agents.visualizer_agent import VisualizerAgent
from agents.banter_agent import BanterAgent
from agents.llm_agent import LLMAgent # Nhập bộ não OpenAI
from scripts.tools.web_scraper import WebScout
from scripts.tools.memory_db import StrategyMemory
from colorama import init, Fore, Style

# Khởi tạo màu sắc cho Terminal
init(autoreset=True)

class SunTzuEasyLife:
    def __init__(self):
        # Khởi tạo tất cả các Agents thành phần
        self.scout = ScoutAgent()
        self.strategist = StrategistAgent()
        self.visualizer = VisualizerAgent()
        self.banter = BanterAgent()
        self.memory = StrategyMemory()
        self.web_scout = WebScout()
        self.llm = LLMAgent() # Bộ não OpenAI
        
        # Cấu hình đường dẫn dữ liệu
        self.root = "Sun_Tzu_Easy_Life"
        self.domains = {
            "financial": "core/phap_systems",
            "social": "core/dia_context_business",
            "internal": "core/thien_universal_laws",
            "relational": "core/dao_human_nature",
            "etiquette": "core/phap_systems"
        }
        print(Fore.CYAN + Style.BRIGHT + "--- [Agent Sun Tzu_Easy_Life: All Systems Online with OpenAI Brain] ---")


    


    def handle_shortcuts(self, query):
        """Xử lý nhanh các yêu cầu về lười/mệt."""
        if any(word in query.lower() for word in ["lazy", "procrastinate", "tired", "lười", "mệt"]):
            path = 'core/tuong_management/procrastination_cheat_sheet.md'
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()
        return None

    def retrieve_knowledge(self, domain):
        """Lấy dữ liệu ngữ cảnh từ các file core/."""
        # Nếu domain không khớp, mặc định lấy tuong_management
        sub_path = self.domains.get(domain, "core/tuong_management")
        full_path = os.path.join(sub_path)
        
        # Tìm file .md đầu tiên trong thư mục đó để làm context
        if os.path.exists(full_path):
            files = [f for f in os.listdir(full_path) if f.endswith('.md')]
            if files:
                with open(os.path.join(full_path, files[0]), 'r', encoding='utf-8') as f:
                    return f.read()
        return "No specific core knowledge found for this theater."

    def execute_command(self, query):
        # 1. Kiểm tra shortcut (lười/mệt)
        shortcut = self.handle_shortcuts(query)
        if shortcut: return {"Shortcut_Advice": shortcut}

        # 2. Scout phân tích Domain (Terrain)
        intel = self.scout.conduct_reconnaissance(query)
        
        # 3. Lấy dữ liệu thực tế từ folder core/ và data/ làm Context cho AI
        knowledge_context = self.retrieve_knowledge(intel['domain'])
        
        tactical_data = ""
        if os.path.exists('data/tactical_library.md'):
            with open('data/tactical_library.md', 'r', encoding='utf-8') as f:
                tactical_data = f.read()

        # 4. Gửi sang cho OpenAI "tư duy" chiến lược
        print(Fore.YELLOW + f"--- [Quân sư đang suy ngẫm kế sách cho: {intel['domain']}] ---")
        try:
            ai_response = self.llm.think(query, knowledge_context, tactical_data)
        except Exception as e:
            ai_response = f"Lỗi kết nối OpenAI: {e}. Vui lòng kiểm tra API Key."

        # 5. Ghi lại vào bộ nhớ (Memory)
        self.memory.record_victory(query, "AI Strategy")

        return {
            "Theater": intel['domain'].upper(),
            "Sun_Tzu_Counsel": ai_response,
            "Sage_Closing": self.banter.crack_joke()
        }

if __name__ == "__main__":
    agent = SunTzuEasyLife()
    
    print(Fore.GREEN + "\n--- CHÀO MỪNG ĐẾN VỚI HỌC VIỆN QUÂN SỰ SỐ (AI VERSION) ---")
    print(Fore.YELLOW + "Nhập vấn đề của bạn (Gõ 'exit' để thoát, 'clear' để xóa màn hình).")

    while True:
        user_input = input(Fore.MAGENTA + "\n[Khách hàng]: " + Fore.WHITE)

        if user_input.lower() == 'exit':
            print(Fore.RED + "Quân sư lui quân. Hẹn gặp lại!")
            break
        
        if user_input.lower() == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if not user_input.strip():
            continue

        try:
            final_output = agent.execute_command(user_input)
            if "Shortcut_Advice" in final_output:
                print(Fore.WHITE + "\n" + final_output["Shortcut_Advice"])
            else:
                print(Fore.CYAN + "\n[Kế Sách Của Quân Sư]:")
                # In ra phản hồi của AI một cách đẹp đẽ
                if "Sun_Tzu_Counsel" in final_output:
                    print(Fore.WHITE + final_output["Sun_Tzu_Counsel"])
                    print(Fore.BLUE + "\n---")
                    print(Fore.YELLOW + "Lời bình: " + final_output["Sage_Closing"])
                else:
                    print(json.dumps(final_output, indent=4, ensure_ascii=False))
                
        except Exception as e:
            print(Fore.RED + f"Lỗi hệ thống: {e}")
