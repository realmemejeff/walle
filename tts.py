from outetts.v0_1.interface import InterfaceHF, InterfaceGGUF
import sys

argumen = sys.argv[1]
interface = InterfaceHF("OuteAI/OuteTTS-0.1-350M")
output = interface.generate(
    text=argumen,
    temperature=0.1,
    repetition_penalty=1.1,
    max_length=4096
)
output.play()
