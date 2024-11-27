from cx_Freeze import setup, Executable

setup(
    name="BillGenerator",
    version="1.0",
    description="Your App Description",
    executables=[Executable("AudioBillGenerator .py")],
)
