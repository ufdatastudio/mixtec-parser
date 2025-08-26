
import sys
from main import parseScene

def test_all_scenes():
    expected_outputs = [
        "in Year 5 House Lord 4 Wind consulted Lady 10 Serpent",
        "in Year 5 House Lord 4 Wind married Lady 10 Serpent",
        "in Year 5 House Lord 4 Wind and Lord 6 Death participated in a ritual sacrifice",
        "in Year 5 House Lord 4 Wind fought Lord 6 Death"
    ]

    input_files = [
        "Scenes/Scene1.xml",
        "Scenes/Scene2.xml",
        "Scenes/Scene3.xml",
        "Scenes/Scene4.xml"
    ]

    for i, (scene_path, expected) in enumerate(zip(input_files, expected_outputs), start=1):
        print(f"\n--- Testing Scene {i} ---")
        sys.argv = ["main.py", scene_path]  # Simulate command-line args
        output = parseScene()
        print("Output:", output)
        assert expected in output, f"❌ Scene {i} failed. Expected: {expected}, Got: {output}"
        print(f"✅ Scene {i} passed.")

if __name__ == "__main__":
    test_all_scenes()
    print("\n🎉 All scenes passed!")
