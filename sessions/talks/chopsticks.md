title: 'Scripting across hosts with Chopsticks'
subtitle: 'Pythonic orchestration over SSH'
speaker: daniel-pope
video: https://www.youtube.com/watch?v=0B3axZrKUQE
---
Chopsticks lets your import and run Python code on remote Unix hosts over SSH.
It works with no code deployment and no preinstalled software other than Python
and SSH. It has built-in support for running code on many hosts in parallel.

Unlike Fabric or Ansible, Chopsticks not opinionated about the structure of the
code you run, allowing it to be used for orchestration, auditing, diagnostics,
monitoring probes, and more.

Also unlike these, Chopsticks is not wedded to SSH, so it can transparently
work on Docker containers over pipes, local subprocesses - and in future, sudo?

Daniel will demonstrate Chopsticks in action, walk through the API, and
explain the three clever tricks that Chopsticks is built on.
