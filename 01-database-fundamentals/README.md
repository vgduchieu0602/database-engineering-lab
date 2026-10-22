# Concept 01 - Tại sao chúng ta cần database?

## Problem

Một mảng lưu trữ trong bộ nhớ sẽ mất dữ liệu khi tiến trình Nodejs kết thúc

## Experiment

1. Tạo 1 array
2. Đẩy 1 user vào đó
3. Dừng tiến trình
4. Khởi động lại tiến trình
5. Người dùng được đẩy vào mảng đã mất

## What I learned

- Mảng có thể lưu trữ và thao tác dữ liệu trong bộ nhớ.
- Bộ nhớ của của tiến trình không cung cấp khả năng lưu trữ lâu dài (persistence).
- Các ứng dụng thường cần dữ liệu tồn tại qua các lần khởi động lại.
- Lưu trữ lâu dài (persistent storage) là cần thiết để dữ liệu không bị mất.