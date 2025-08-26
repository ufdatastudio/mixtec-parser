import sys
from main import parseScenes

def test_all_scenes():
    # Dictionary mapping file paths to expected outputs
    test_cases = {
        "Scenes/Scene1.xml": "in Year 5 House Lord 4 Wind consulted Lady 10 Serpent",
        "Scenes/Scene2.xml": "in Year 5 House Lord 4 Wind married Lady 10 Serpent",
        "Scenes/Scene3.xml": "in Year 5 House Lord 4 Wind and Lord 6 Death participated in a ritual sacrifice",
        "Scenes/Scene4.xml": "in Year 5 House Lord 4 Wind fought Lord 6 Death",
        "Scenes/Scene5.xml": "in Year 5 House Lord 4 Wind fought Lord 6 Death. . in Year 5 House Lord 4 Wind and Lord 6 Death participated in a ritual sacrifice"
    }

    for i, (file_path, expected_output) in enumerate(test_cases.items(), start=1):
        sys.argv = ["main.py", "-rd", file_path]  # Simulate command-line arguments
        output = parseScenes()
        assert expected_output in output, f"❌ Scene {i} failed.\nExpected: {expected_output}\nGot: {output}"
        print(f"✅ Scene {i} passed.")

if __name__ == "__main__":
    test_all_scenes()
    print("\n🎉 All scenes passed!")
