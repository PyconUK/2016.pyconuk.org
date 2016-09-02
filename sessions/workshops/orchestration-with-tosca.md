title: Orchestration with TOSCA
speaker: denys-makogon
---
AIOrchestra is the way to rethink the way we develop and deploy. The idea that stands behind it - open platform, open capabilities, open TOSCA. While AIOrchestra being an engine to process TOSCA models into executable deployment graph using Python 3.5 and its asynchronous API.
The hardest part of AIOrchestra was to convert TOSCA models into an executable object. Based on TOSCA understanding it was required to have asynchronous tasks that may run in parallel but having common synchronization point between them.
Starting version 3.4, Python standard library provides asynchronous API using event-driven handling concept through coroutines. This is exact technology above which AIOrchestra is built. So, this talk will discover exact lesson that we’ve learnt while building dynamic graph of sequenced asynchronous tasks to accomplish concrete result - do a consistent asynchronous deployment orchestration.

Problem addressing

This talk addressing problems of:
 - building complex frameworks asynchronous frameworks and its extensions
 - understanding existing IO-bound API problem on the example of OpenStack SDK and AsyncSSH API
 - building sequenced asynchronous task graph
 - building sequenced task graph versus asynchronous pipeline graph

What attendees will expect to learn?

Key things that attendees will learn during talk:
 - OASIS TOSCA and AIOrchestra as an execution engine implementation
 - key concept of AIOrchestra
 - why IO-bound operations are so important for AIOrchestra underlying concept
 - AIOrchestra extensions how-to’s
 - AIOrchestra use cases: Infrastructure and Software orchestration
