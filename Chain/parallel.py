from pandas.core.window.doc import template_returns
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()
api_key_1 = os.getenv("OPENROUTER_API_KEY")
api_key_2 = os.getenv("Laguna")

model_1 = ChatOpenAI(
   model = 'tencent/hy3:free',
    api_key=api_key_1,
    temperature=0,
    base_url="https://openrouter.ai/api/v1"

)


model_2 = ChatOpenAI(
   model = 'poolside/laguna-m.1:free',
    api_key=api_key_2,
    temperature=0,
    base_url="https://openrouter.ai/api/v1"
)

temp_1 = PromptTemplate(
    template= "Make Short notes using this : {text}",
    input_variables=['text']
)

temp_2 = PromptTemplate(
    template='Make question answer using this {text}',
    input_variables=['text']
)

temp_3 = PromptTemplate(
    template='Make a single document merging these 2 texts {notes} and {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
    'notes' : temp_1|model_1|parser,
    'quiz': temp_2|model_1|parser
    }
)


sequential_chain = temp_3|model_1|parser


chain = parallel_chain|sequential_chain

result = chain.invoke({'text':""" Quantum mechanics (QM) is the fundamental theory in physics that describes nature at the smallest scales of energy levels of atoms and subatomic particles.

To understand quantum mechanics, you must first unlearn your everyday intuition. In the macroscopic world—the world of apples, cars, and planets—classical physics (Newton’s laws) reigns supreme. Things are predictable, deterministic, and exist in definite states. Quantum mechanics throws all of that out the window.

Here is a detailed, step-by-step breakdown of the core concepts, experiments, and implications of quantum mechanics.

---

### 1. Why was Quantum Mechanics Invented?
By the late 19th century, classical physics thought it had almost solved the universe. But a few nagging problems refused to go away:
*   **The Ultraviolet Catastrophe:** Classical physics predicted that a hot object (like a star or a lightbulb filament) would emit infinite amounts of high-energy ultraviolet light. This is obviously wrong.
*   **The Photoelectric Effect:** Shining light on a piece of metal should eventually knock electrons off it, regardless of the light's color (according to classical physics). But experiments showed that only high-frequency (blue/violet) light worked, while low-frequency (red) light did nothing, no matter how bright it was.
*   **Atomic Stability:** According to classical electromagnetism, electrons orbiting a nucleus should constantly lose energy and spiral into the nucleus in a fraction of a second. Yet, atoms are incredibly stable.

Classical physics was broken at the microscopic level. A new framework was required.

---

### 2. The Core Principles (The "Weirdness")

#### A. Quantization
Energy does not flow continuously like water from a faucet; it comes in discrete packets called **quanta** (singular: quantum). Imagine walking up a flight of stairs versus walking up a ramp. On a ramp, you can stop at any height. On stairs, you can only stand on specific steps. In the quantum world, energy levels are like stairs. This solved the Ultraviolet Catastrophe (Max Planck) and the Photoelectric Effect (Albert Einstein).

#### B. Wave-Particle Duality
In the classical world, things are either a wave (like sound or ripples in a pond) or a particle (like a marble). In the quantum world, **everything is both**.
*   Light, previously thought to be strictly a wave, acts like a particle (the photon).
*   Electrons, previously thought to be strictly particles (tiny spheres), act like waves. They can diffract and interfere with one another, just like water waves.

#### C. Superposition
Until it is measured, a quantum system does not exist in a single, definite state. Instead, it exists in a combination of all possible states simultaneously.
*   *Analogy:* Think of a spinning coin. While it is spinning, is it heads or tails? It is a blur of both. Only when you slap it down and look at it (measure it) does it "choose" a state.

#### D. The Uncertainty Principle
Formulated by Werner Heisenberg, this principle states that you cannot simultaneously know both the exact position and the exact momentum (speed + direction) of a quantum particle.
*   *Analogy:* Imagine taking a photograph of a moving car. If you use a fast shutter speed, you know exactly where the car is, but the picture is dark, so you can't tell how fast it's going. If you use a slow shutter speed, you can see the motion blur to know its speed, but the car is smeared across the image, so you don't know its exact position.
*   *Crucial note:* This is not a limitation of our measuring tools. It is a fundamental property of the universe. The particle literally does not possess a definite position and definite momentum at the same time.

#### E. Entanglement
When two particles become entangled, they form a single quantum system. If you measure the state of Particle A, you instantly know the state of Particle B, regardless of how far apart they are—even if they are on opposite sides of the universe. Einstein famously hated this, calling it "spooky action at a distance," because it seems to violate the cosmic speed limit (the speed of light). However, decades of experiments have proven it is entirely real. *(Note: Entanglement cannot be used to send information faster than light).*

---

### 3. The Mathematical Framework (Conceptual)

How do physicists calculate all this? They use the **Wavefunction**, represented by the Greek letter Psi ($\Psi$).

*   **The Wavefunction:** This is a mathematical wave that spreads out through space. It contains all the information about a quantum system.
*   **The Born Rule:** The wavefunction doesn't tell you exactly where a particle is. Instead, the square of the wave's amplitude ($|\Psi|^2$) gives the **probability** of finding the particle in a specific location if you look for it.
*   **The Schrödinger Equation:** This is the quantum equivalent of $F=ma$ (Newton’s Second Law). It dictates how the wavefunction evolves and changes over time. It is incredibly accurate.
*   **Wavefunction Collapse:** When you finally measure the particle, the spread-out probability wave instantly "collapses" into a single, definite point.

---

### 4. The Defining Experiment: The Double-Slit Experiment
No concept in QM is better illustrated than the Double-Slit Experiment. Imagine a barrier with two narrow slits, and a detector screen behind it.

1.  **Fire Marbles (Classical Particles):** The marbles go through one slit or the other, hitting the wall and forming two distinct bands on the screen.
2.  **Send Water Waves (Classical Waves):** The waves go through both slits, creating ripples that crash into each other (interference). This creates a complex pattern of many alternating bright and dark bands on the screen.
3.  **Fire Electrons one at a time (Quantum):** You fire a single electron. It hits the screen as a single dot (a particle). You fire another, it hits somewhere else. But after firing thousands of them, a pattern emerges on the screen: **the wave interference pattern**.
    *   *The mind-bending conclusion:* Even though the electrons were fired one at a time, each individual electron somehow traveled through *both slits*, interfered with *itself*, and then randomly chose where to land based on the probability wave.
4.  **The ultimate weirdness:** If you place a detector at the slits to see which slit the electron goes through, the interference pattern vanishes. The electrons suddenly act like classical marbles, forming just two bands. **The act of observing the system changes its behavior.**

---

### 5. The Interpretations: What Does It Mean?
The math of quantum mechanics works flawlessly. It is the most rigorously tested theory in human history. However, *what the math actually means* is highly debated. These are called Interpretations:

*   **The Copenhagen Interpretation (The Orthodox View):** Developed by Niels Bohr and Werner Heisenberg. It says that the quantum world is inherently probabilistic. A particle doesn't have a definite property until you measure it. The wavefunction collapse is a real event. "Shut up and calculate."
*   **Many-Worlds Interpretation:** Proposed by Hugh Everett III. It argues that the wavefunction *never* collapses. Instead, every time a measurement is made, the universe splits. In one universe, you found the electron on the left; in another newly created universe, a copy of you found it on the right. All possibilities happen in an infinite multiverse.
*   **Pilot Wave Theory (De Broglie-Bohm):** Brings determinism back. It suggests particles are real physical objects guided by a hidden "pilot wave." However, it requires the universe to be "non-local" (instantaneous connections across space), which bothered Einstein.
*   **Quantum Decoherence:** A modern addition that explains *how* the classical world emerges from the quantum world. A quantum particle interacting with a macroscopic environment (like air molecules or heat) quickly loses its quantum properties (decoheres), making it look classical to us.

---

### 6. Real-World Applications
Quantum mechanics isn't just abstract philosophy; it is the engine of the modern world. Without understanding QM, we could not have built:
*   **Semiconductors & Transistors:** The computer, smartphone, or device you are reading this on relies on the quantum behavior of electrons in silicon.
*   **Lasers:** The stimulated emission of photons is a purely quantum mechanical process. Used in everything from fiber optics to surgery.
*   **MRI Machines:** Magnetic Resonance Imaging relies on flipping the quantum "spin" of hydrogen atoms in your body.
*   **Atomic Clocks:** The basis of GPS satellites. They measure the exact frequency of microwave radiation required to make electrons in a cesium atom "jump" between quantum energy levels.
*   **Quantum Computing:** The next frontier. While classical computers use bits (0 or 1), quantum computers use "qubits" which utilize superposition to be 0 and 1 simultaneously, and entanglement to solve certain complex problems (like drug discovery and cryptography) exponentially faster than classical computers.

### Summary
Quantum mechanics reveals a universe at its foundational level that is blurry, probabilistic, and deeply interconnected. It suggests that the "solid" world we experience every day is just a macroscopic illusion—a statistical averaging of a chaotic, dancing quantum reality beneath it. As physicist Richard Feynman famously said, *"If you think you understand quantum mechanics, you don't understand quantum mechanics."*    """})



print(result)

print("\n--------------------------------------------------------\n")

chain.get_graph().print_ascii()