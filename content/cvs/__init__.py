"""Danh sách toàn bộ CV.

Thêm CV mới: tạo một file trong thư mục này (theo mẫu các file có sẵn),
rồi thêm vào CVS bên dưới.
"""
from . import ai_automation, backend_dotnet, devops, frontend_react, fullstack, software_engineer

CVS = [
    fullstack.CV,
    software_engineer.CV,
    backend_dotnet.CV,
    frontend_react.CV,
    devops.CV,
    ai_automation.CV,
]
