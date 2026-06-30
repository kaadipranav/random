import os
import sys
import ast
import time
import random

# --- ANSI Escape Codes ---
class Colors:
    HEADER = '\033[96m'       # Cyan
    SUCCESS = '\033[92m'      # Green
    WARNING = '\033[93m'      # Yellow
    ERROR = '\033[91m'        # Red
    INPUT = '\033[94m'        # Blue
    DIM = '\033[2m'           # Dim
    BOLD = '\033[1m'          # Bold
    RESET = '\033[0m'         # Reset
    BLINK = '\033[5m'         # Blink
    UNDERLINE = '\033[4m'     # Underline

# --- KAADZ Extreme Branding ---
LOGO_ASCII = f"""
{Colors.HEADER}
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░  ░░░░  ░░░░░░░░░      ░░░░░░░░░░      ░░░░░░░░░       ░░░░░░░░░        ░
▒  ▒▒▒  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒
▓     ▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓
█  ███  █████████        ████████        ████████  ████  █████████  ██████
█  ████  ████████  ████  ████████  ████  ████████       █████████        █
██████████████████████████████████████████████████████████████████████████ 

   {Colors.DIM}>> R e c o r d   P r o g r a m   1 6 <<{Colors.RESET}
"""

FOOTER_ASCII = f"""
{Colors.DIM}
──────────────────────────────────────────────────────────────────────
{Colors.HEADER}KAADZ{Colors.RESET} | {Colors.DIM}System Status: {Colors.SUCCESS}ONLINE{Colors.DIM} | {Colors.INPUT}Ready{Colors.RESET}
──────────────────────────────────────────────────────────────────────
"""

# --- Animation Helpers ---

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, color=Colors.RESET, delay=0.03):
    """Prints text character by character with a color."""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(label, duration=1.5, symbol="█", empty_symbol="░"):
    """Simulates a loading bar with animation."""
    width = 40
    steps = 20
    delay = duration / steps
    
    sys.stdout.write(f"\n{Colors.HEADER}{label}{Colors.RESET} [")
    sys.stdout.flush()
    
    for i in range(steps + 1):
        filled = int(width * i / steps)
        bar = symbol * filled + empty_symbol * (width - filled)
        sys.stdout.write(f"\r{Colors.HEADER}{label}{Colors.RESET} [{bar}] {i*5}%")
        sys.stdout.flush()
        time.sleep(delay)
    
    print(f"\r{Colors.HEADER}{label}{Colors.RESET} [{symbol * width}] 100% {Colors.SUCCESS}✓ Done{Colors.RESET}")
    time.sleep(0.3)

def spinner_animation(label, duration=1.0):
    """Spins a loader while processing."""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    
    while time.time() < end_time:
        for frame in frames:
            sys.stdout.write(f"\r{Colors.HEADER}{frame} {label}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write(f"\r{Colors.SUCCESS}✓ {label} Complete{Colors.RESET}\n")
    time.sleep(0.2)

def glitch_effect(text, color=Colors.ERROR):
    """Simulates a glitch effect on text."""
    sys.stdout.write(f"\n{color}⚠ {text} ⚠{Colors.RESET}\n")
    sys.stdout.flush()
    time.sleep(0.1)
    for _ in range(3):
        sys.stdout.write(f"\r{Colors.DIM}{' ' * 50}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
        sys.stdout.write(f"\r{color}⚠ {text} ⚠{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def draw_box(title, lines, width=55):
    """Draws a styled box with glowing borders."""
    top = f"{Colors.HEADER}╭{'─' * (width - 2)}╮{Colors.RESET}"
    mid = f"{Colors.HEADER}│{Colors.RESET} {title:^{width-4}} {Colors.HEADER}│{Colors.RESET}"
    divider = f"{Colors.HEADER}├{'─' * (width - 2)}┤{Colors.RESET}"
    bot = f"{Colors.HEADER}╰{'─' * (width - 2)}╯{Colors.RESET}"
    
    print(f"\n{top}")
    print(mid)
    print(divider)
    for line in lines:
        print(f"{Colors.HEADER}│{Colors.RESET} {line:<{width-4}} {Colors.HEADER}│{Colors.RESET}")
    print(bot)
    print()

def draw_header():
    clear_screen()
    print(LOGO_ASCII)
    print(f"{Colors.DIM}{'─' * 60}{Colors.RESET}")
    print()

def draw_footer():
    print()
    print(f"{Colors.DIM}{'─' * 60}{Colors.RESET}")
    print(FOOTER_ASCII)

# --- Core Logic ---

def input_colored(prompt):
    print(f"\n{Colors.INPUT}➜ {Colors.RESET}{prompt}", end="")
    try:
        raw = input()
        return ast.literal_eval(raw)
    except (ValueError, SyntaxError):
        glitch_effect("Invalid Input Format")
        return None

def push_to_stack(user_stack, stack_to_push):
    spinner_animation("Processing Push Operation...")
    user_stack.append(stack_to_push)
    typewriter(f"   ✓ Element Pushed: {stack_to_push}", Colors.SUCCESS)

def pop_element(user_stack):
    if not user_stack:
        glitch_effect("Stack Underflow! Empty Stack.")
        return
    spinner_animation("Popping Element...")
    popped = user_stack.pop()
    typewriter(f"   ✓ Element Popped: {popped}", Colors.SUCCESS)

def traverse_stack(user_stack):
    print(f"\n{Colors.HEADER}   SCANNING STACK MEMORY...{Colors.RESET}")
    loading_bar("Data Retrieval", duration=1.0)
    
    if not user_stack:
        glitch_effect("No Data Found in Stack")
        return

    print(f"\n{Colors.HEADER}   ┌──────── STACK DUMP ────────┐{Colors.RESET}")
    for i, item in enumerate(reversed(user_stack)):
        real_index = len(user_stack) - 1 - i
        sys.stdout.write(f"\r   │ [{real_index}] {item}...")
        sys.stdout.flush()
        time.sleep(0.05)
    print(f"{Colors.HEADER}   └────────────────────────────┘{Colors.RESET}\n")

def peek_stack(user_stack):
    if not user_stack:
        glitch_effect("Stack Empty! Cannot Peek.")
        return
    
    spinner_animation("Locating Top Element...")
    last_element = user_stack[-1]
    index = len(user_stack) - 1
    typewriter(f"   ⚠ Top: {Colors.BOLD}{last_element}{Colors.RESET} | Index: {Colors.BOLD}{index}{Colors.RESET}", Colors.WARNING)

def show_menu():
    draw_header()
    menu_items = [
        "1. [PUSH] Inject Data",
        "2. [POP] Extract Data",
        "3. [TRAVERSE] Scan Memory",
        "4. [PEEK] View Top Element",
        "5. [EXIT] Terminate System"
    ]
    draw_box("SYSTEM MENU", menu_items, width=55)
    
    print(f"{Colors.INPUT}➜ {Colors.RESET}Command: ", end="")
    try:
        return int(input())
    except ValueError:
        return -1

def main():
    initial_stack = []
    
    # Boot Sequence
    clear_screen()
    print(LOGO_ASCII)
    typewriter("Initializing KAADZ Stack System...", Colors.HEADER, 0.05)
    loading_bar("Loading Modules", duration=1.5)
    spinner_animation("Checking Dependencies")
    typewriter("System Ready.", Colors.SUCCESS)
    time.sleep(1)
    
    clear_screen()
    draw_header()
    typewriter("Welcome, Operator.", Colors.HEADER, 0.05)
    
    start_input = input_colored("Enter initial stack (e.g., ['FL1', 'AirlineA']): ")
    if start_input and isinstance(start_input, list):
        initial_stack = start_input
        typewriter("   ✓ Initial Data Loaded.", Colors.SUCCESS)
    else:
        typewriter("   ℹ Starting with Empty Stack.", Colors.DIM)
        initial_stack = []
    
    input(f"\n{Colors.DIM}Press Enter to Engage...{Colors.RESET}")
    
    while True:
        choice = show_menu()
        
        if choice == 1:
            draw_header()
            typewriter(">>> INITIATING PUSH SEQUENCE", Colors.HEADER)
            new_item = input_colored("Enter Data Pair: ")
            if new_item:
                push_to_stack(initial_stack, new_item)
            input(f"\n{Colors.DIM}Press Enter to Continue...{Colors.RESET}")
            
        elif choice == 2:
            draw_header()
            typewriter(">>> INITIATING POP SEQUENCE", Colors.HEADER)
            pop_element(initial_stack)
            input(f"\n{Colors.DIM}Press Enter to Continue...{Colors.RESET}")
            
        elif choice == 3:
            draw_header()
            typewriter(">>> INITIATING SCAN SEQUENCE", Colors.HEADER)
            traverse_stack(initial_stack)
            input(f"\n{Colors.DIM}Press Enter to Continue...{Colors.RESET}")
            
        elif choice == 4:
            draw_header()
            typewriter(">>> INITIATING PEEK SEQUENCE", Colors.HEADER)
            peek_stack(initial_stack)
            input(f"\n{Colors.DIM}Press Enter to Continue...{Colors.RESET}")
            
        elif choice == 5:
            draw_header()
            typewriter(">>> INITIATING SHUTDOWN SEQUENCE", Colors.WARNING)
            loading_bar("Terminating Processes", duration=1.0)
            clear_screen()
            print(LOGO_ASCII)
            typewriter("System Halted. Goodbye.", Colors.ERROR)
            draw_footer()
            break
            
        else:
            draw_header()
            glitch_effect("INVALID COMMAND DETECTED")
            input(f"\n{Colors.DIM}Press Enter to Retry...{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        draw_header()
        typewriter("Force Stop Interrupted.", Colors.ERROR)
        draw_footer()
        sys.exit(0)
