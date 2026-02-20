#!/bin/bash
dnf update -y && \
dnf install -y git && \
curl -fsSL https://rpm.nodesource.com/setup_
23.x | bash - && \
dnf install -y nodejs && \
git clone https://gitlab.com/ftutorials-labs/quiz-ansible.git && \
cd quiz-ansible && \
npm install && \
npm run build && \
npm install -g serve && \
serve -s dist
