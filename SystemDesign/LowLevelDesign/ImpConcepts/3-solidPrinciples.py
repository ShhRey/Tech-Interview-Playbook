# SOLID is an acronym for five foundational principles of object-oriented design, introduced by Robert C. Martin ("Uncle Bob"). 

'''
#============================================================================== 1. Single Responsibility Principle ========================================================================#
A class should have one, and only one, reason to change!    What is a Responsibility? It's not a method. It's not a function. It's a reason for the class to change.
This means every class, function, or module should do one thing only — and do it well. If a class has more than one responsibility, changes to one responsibility can affect or break the other.

Why does SRP matter?
- Easier to read: You immediately understand what the class is supposed to do. No surprises.
- Easier to test: Smaller responsibilities mean smaller test cases and fewer dependencies.
- Easier to reuse: Small, focused classes are more flexible and can be reused in different contexts.
- Scales better: Teams can own different parts of the system without stepping on each other's toes.

Common Pitfalls while applying SRP:
- Over Splitting Responsibilities: Too many tiny classes that dont add real value.
- Confusing Method with Responsibility: Assuming each method must be in its own class.
- Ignoring Small Utility Classes: Underestimating Smaller Class and not splitting them.
'''
# Creating Single Responsibility Class (New Employee)
class Employee:
    def __init__(self, name: str, email: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    # Getter Methods/Functions to Access Private Attributes
    def get_name(self) -> str:
        return self._name
    def get_base_salary(self) -> float:
        return self._base_salary


# Class that handles Payroll Policy for the Employee
class PayrollCalculator:
    def calculate_net_pay(self, employee: Employee) -> float:
        base = employee.get_base_salary()
        tax = base * 0.2  # Sample tax logic
        benefits = 1000   # Fixed benefit deduction
        return base - tax + benefits

# Class that handles Payslip Generation for the Employee
class PayslipGenerator:
    def generate_payslip(self, employee: Employee, net_pay: float) -> str:
        return (
            f"Payslip for: {employee.get_name()}\n"
            f"Email: {employee.get_email()}\n"
            f"Net Pay: ${net_pay}\n"
            "----------------------------\n"
        )




'''
#============================================================================== 2. Open-Close Principle ==================================================================================#
Any software entity (classes, modules, functions, etc.) should be open for extension but closed for modification. We can use inheritance and polymorphism to solve this.
Open for Extension: As new requirements come in (like new payment types), you should be able to add new behavior.
Closed for Modification: Once it's written, tested, and working, you shouldn't need to go back and alter it to add new features.

Why does OCP matter?
- Improved Maintainability: By adding new code rather than changing old code, you reduce risk of breaking functionality.
- Enhanced Scalability: Your codebase becomes more flexible and adaptable to change.
- Reduced Risks: The chances of introducing regressions (bugs in old features) are significantly lower.
- Better Testability: New extensions can be tested in isolation.

Common Pitfalls while applying OCP:
- Overuse / Premature Abstraction: Can lead to overly complex designs and unnecessary abstractions.
- Misinterpreting OCP:  If there's a bug in the existing code, you absolutely must fix it.
'''
# Importing Necessary Libraries for Abstraction
from abc import ABC, abstractmethod

# Defining an Interface / Abstract Class
class Employee(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

# Specific Employee Type extending our Abstract Class
class FullTimeEmployee(Employee):
    def __init__(self, name: str, salary: float):
        # Inheriting the constructor from Parent
        super().__init__(name)
        self.salary = salary
    
    def calculate_salary(self) -> float:
        return self.salary
    
# Specific Employee Type extending our Abstract Class
class Contractor(Employee):
    def __init__(self, name: str, hourly_rate: float, hours_worked: float):
        # Inheriting the constructor from Parent
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self) -> float:
        return self.hourly_rate * self.hours_worked


# The SalaryCalculator is now closed for Modification
class SalaryCalculator:
    def calculate_total_salary(self, employees: list) -> float:
        total = 0
        # Overriding the Abstract Method implementing Polymorphism
        for employee in employees:
            total += employee.calculate_salary()
        return total




'''
#============================================================================== 3. Liskov Substitution Principle ========================================================================#
If B is a subtype of A, then objects of type A may be replaced with objects of type B without altering any of the desirable properties of that program (correctness, task performed, etc).
Subtypes must honor the expectations set by their base types; The client code shouldn't need to know or care which specific subtype it's dealing with.

Why does LSP matter?
- Reliability and Predictability: You can substitute any subtype and still get the behavior your client code expects.
- True Polymorphism: LSP is what makes polymorphism truly powerful. You can write generic algorithms.
- Testability: Tests written for the base class's interface should work for all its subtypes.

Common Pitfalls while applying LSP:
- Is-A Trap: Just because something sounds like it “is a”, it doesn't mean it's a valid subtype in code.
- Precondition: The subtype requires more than the base class contract promised.
- Postcondition: The subtype delivers less than the base class guaranteed.
'''
# Define Different Interfaces depending on Behavior
class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

class Editable(ABC):
    @abstractmethod
    def save(self, new_data):
        pass


# Concreting Different Types to Overwrite our Interfaces
class EditableDocument(Document, Editable):
    def __init__(self, data):
        self.data = data

    def open(self):
        print("Editable Document opened. Data:", self._preview())

    def save(self, new_data):
        self.data = new_data
        print("Document saved.")

    def get_data(self):
        return self.data

    def _preview(self):
        return self.data[:20] + "..."
    
class ReadOnlyDocument(Document):
    def __init__(self, data):
        self.data = data

    def open(self):
        print("Read-Only Document opened. Data:", self._preview())

    def get_data(self):
        return self.data

    def _preview(self):
        return self.data[:20] + "..."
    

# Update Document Processor to Act According to 
class DocumentProcessor:
    def process(self, doc: Document):
        doc.open()
        print("Document processed.")

    def process_and_save(self, doc: Document, additional_info: str):
        if not isinstance(doc, Editable):
            raise ValueError("Document is not editable.")

        doc.open()
        current_data = doc.get_data()
        new_data = current_data + " | Processed: " + additional_info
        doc.save(new_data)
        print("Editable document processed and saved.")

    def process_editable_document(self, editable_doc: Editable, doc: Document, additional_info: str):
        doc.open()
        current_data = doc.get_data()
        new_data = current_data + " | Processed: " + additional_info
        editable_doc.save(new_data)
        print("Editable document processed and saved.")



'''
#============================================================================== 4. Interface Segregation Principle ======================================================================#
ISP states that no client should be forced to depend on methods it does not use. This means you should create small, specific interfaces rather than one large, general-purpose one.
Clients should not be forced to depend on methods they do not use. Keep your interfaces focused. Each interface should represent a specific capability or behavior.

Why does ISP matter?
- Increased Cohesion, Reduced Coupling: Interfaces become highly focused. This minimizes unnecessary dependencies.
- Improved Flexibility & Reusability: Smaller, role-specific interfaces are easier for classes to implement correctly.
- Avoid "Interface Pollution" and LSP Violations: Classes aren't forced to implement methods they don't need, drastically reducing the likelihood of UnsupportedOperationExceptions and making subtypes more reliably substitutable for the interfaces they claim to implement.

Common Pitfalls while applying ISP:
- Client Perspective: Designing interfaces based only on how implementers work — not how clients use them.
- Lack of Cohesion: Creating interfaces that aren't tightly related; mixing unrelated methods together.
'''
# Defining Small Cohesive Interfaces / Abstract Classes
# 1. Audio Focused Media Player
class AudioPlayerControls(ABC):
    @abstractmethod
    def play_audio(self, audio_file):
        pass

    @abstractmethod
    def stop_audio(self):
        pass

    @abstractmethod
    def adjust_audio_volume(self, volume):
        pass

# 2. Video Focused Media Player
class VideoPlayerControls(ABC):
    @abstractmethod
    def play_video(self, video_file):
        pass

    @abstractmethod
    def stop_video(self):
        pass

    @abstractmethod
    def adjust_video_brightness(self, brightness):
        pass

    @abstractmethod
    def display_subtitles(self, subtitle_file):
        pass

# Overriding AudioPlayerControls to create a Audio-Only Player
class ModernAudioPlayer(AudioPlayerControls):
    def play_audio(self, audio_file):
        print(f"ModernAudioPlayer: Playing audio - {audio_file}")

    def stop_audio(self):
        print("ModernAudioPlayer: Audio stopped.")

    def adjust_audio_volume(self, volume):
        print(f"ModernAudioPlayer: Volume set to {volume}")

# Overriding VideoPlayerControls to create a Video-Only Player
class NormalVideoPlayer(VideoPlayerControls):
    def play_video(self, video_file):
        print(f"NormalVideoPlayer: Playing video - {video_file}")

    def stop_video(self):
        print("NormalVideoPlayer: Video stopped.")

    def adjust_video_brightness(self, brightness):
        print(f"NormalVideoPlayer: Brightness set to {brightness}")

    def display_subtitles(self, subtitle_file):
        print(f"NormalVideoPlayer: Subtitles from {subtitle_file}")

# Overriding AudioPlayerControls and VideoPlayer to create a Combo-MediaPlayer
class ComprehensiveMediaPlayer(AudioPlayerControls, VideoPlayerControls):
    def play_audio(self, audio_file):
        print(f"ComprehensiveMediaPlayer: Playing audio - {audio_file}")

    def stop_audio(self):
        print("ComprehensiveMediaPlayer: Audio stopped.")

    def adjust_audio_volume(self, volume):
        print(f"ComprehensiveMediaPlayer: Audio volume set to {volume}")

    def play_video(self, video_file):
        print(f"ComprehensiveMediaPlayer: Playing video - {video_file}")

    def stop_video(self):
        print("ComprehensiveMediaPlayer: Video stopped.")

    def adjust_video_brightness(self, brightness):
        print(f"ComprehensiveMediaPlayer: Brightness set to {brightness}")

    def display_subtitles(self, subtitle_file):
        print(f"ComprehensiveMediaPlayer: Subtitles from {subtitle_file}")



'''
#============================================================================== 5. Dependency Inversion Principle ========================================================================#
=> High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g., interfaces).
=> Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.

With DIP, both the high-level module and the low-level module depend on a shared abstraction (an interface or abstract class). 
The control flow might still go from high to low, but the source code dependency is inverted.

Why does DIP matter?
- Decoupling: High-level modules become independent of the nitty-gritty details of low-level modules.
- Flexibility & Extensibility: Just create a new class that implements the shared abstraction. The high-level module doesn't need to change.
- Enhanced Testability: You can easily swap out real dependencies with mock objects or test doubles.
- Parallel Development: Once the abstraction (interface) is defined, different teams can work independently.

Common Pitfalls while applying DIP:
- Over Abstraction: If something is stable and internal, don't abstract it just for the sake of DIP.
- Leaky Abstraction: Interfaces should only expose what the high-level module needs, not what a specific implementation does behind the scenes.
- The abstraction should be defined by the high-level module (or in a neutral shared module), not by the implementation.
'''
# Defining the Abstraction
class EmailClient(ABC):
    @abstractmethod
    def send_email(self, to, subject, body):
        pass

# Let Specific Clients implement the Interface
class GmailClientImpl(EmailClient):
    def send_email(self, to, subject, body):
        print("Connecting to Gmail SMTP server...")
        print(f"Sending email via Gmail to: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        # ... actual Gmail API interaction logic ...
        print("Gmail email sent successfully!")

class OutlookClientImpl(EmailClient):
    def send_email(self, to, subject, body):
        print("Connecting to Outlook Exchange server...")
        print(f"Sending email via Outlook to: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        # ... actual Outlook API interaction logic ...
        print("Outlook email sent successfully!")

# Updating the High-Level Module injecting the EmailClient
class EmailService:
    def __init__(self, email_client: EmailClient):
        self.email_client = email_client

    def send_welcome_email(self, user_email, user_name):
        subject = f"Welcome, {user_name}!"
        body = "Thanks for signing up to our awesome platform. We're glad to have you!"
        self.email_client.send_email(user_email, subject, body)

    def send_password_reset_email(self, user_email):
        subject = "Reset Your Password"
        body = "Please click the link below to reset your password..."
        self.email_client.send_email(user_email, subject, body)