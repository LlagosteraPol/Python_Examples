import language_tool_python


#tool = language_tool_python.LanguageTool('es') # Download locally
tool = language_tool_python.LanguageToolPublicAPI('es') # use the public API, language Spanish
#tool = language_tool_python.LanguageTool('ca-ES', remote_server='https://language-tool-api.mywebsite.net')  # use a remote server API, language Catalan

text = "Uns textor mal exho"
matches = tool.check(text)
for match in matches:
    print(match)

print("Corrected:")
print(tool.correct(text))