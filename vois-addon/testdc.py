import keyboard

def on_key_event(e):
    print(f"Key {e.name} with code {e.scan_code} {'pressed' if e.event_type == keyboard.KEY_DOWN else 'released'}")

keyboard.hook(on_key_event)
keyboard.wait("esc")










