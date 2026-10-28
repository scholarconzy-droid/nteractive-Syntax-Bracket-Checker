class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def _save_state(self):
        # Push current state to undo stack and clear redo stack on new action
        self.undo_stack.append(self.text)
        self.redo_stack.clear()

    def type_text(self, new_text):
        self._save_state()
        self.text += new_text
        print(f"Typed: '{new_text}' -> Current Text: '{self.text}'")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo!")
            return
        # Save current state to redo stack
        self.redo_stack.append(self.text)
        # Pop previous state from undo stack
        self.text = self.undo_stack.pop()
        print(f"Undo performed -> Current Text: '{self.text}'")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo!")
            return
        # Save current state back to undo stack
        self.undo_stack.append(self.text)
        # Pop state from redo stack
        self.text = self.redo_stack.pop()
        print(f"Redo performed -> Current Text: '{self.text}'")


# --- Demonstration ---
editor = TextEditor()
editor.type_text("Hello")
editor.type_text(" World")
editor.undo()          # Reverts " World"
editor.redo()          # Restores " World"
editor.type_text("!")  # Clears redo stack and adds "!"