# When will it be done

> Strive to create something that outlives this course.
>
> -- [CS50x Final Project Description]

## Product Vision

Self-organizing development teams are in control of the way they go about their work.
They are able to connect their way of working
to the needs of the people with a stake in their work.
While going about their work, they reflect and improve: there must be a better way!

The when-will-it-be-done app will allow development teams to 
quickly experiment with different ways to go about their work.
These experiments will allow teams to assess the effects of existing or new work policies -
after a few minutes of coding and simulation.

This app allows development teams to 
see the impact of micro-, everyday decisions in terms of whole-playing-field outcomes.

## Product Specification

### Prerequisites

Python 3.8, optionally a virtual envronment tool (e.g. [Pipenv]). 

### Installation

Clone this repository. 

If you're not using a virtual environment, install the dependencies from [`Pipfile`](./Pipfile).

Verify your installation and setup by running 

```
python ./01_sprint.py
```

Sim away!

### How to use

 1. modify the models to reflect your team's (suggested) work policies
 1. run a simulation
 1. learn from the simulation's output

## Backlogs

### Doing

 * [ ] cycle time histograms

### Product Backlog

 * [ ] Collect output metrics from wwibd
    * flow efficiency
    * throughput
    * CFD
    * start & stop time per work item
 * [ ] Chapter 11 of [Vacanti2000] is a great description on how to get started wth process improvement; 
       it serves as a great way for modelling and simulating too.
 * [ ] Distill sample scenarios from [Vacanti2009]
 * [ ] Simulate a siloed Kanban work group
 * [ ] Simulate a Swarming Scrum Team
 * [ ] Make a collection of interesting agile paradigms to confirm or to falsify
       (cross functional team, T-shaped team members, single piece flow, estimation,
       release early and often, swarming).
 * [ ] Simulate the effect of disruptions and various ways to handle them (e.g. expediting)
 * [ ] Experiment with pull policies
    * Poor policies: ignore blocked items, ignore wip limits, no dod & rework
    * Good (?) policies: e.g. chapter 10 on system stability
 * [ ] Use the simulations you developed in a Monte Carlo Simulation
 * [ ] Plug in your own data into the simulation's distributions
 * [ ] Visualize a system's stability


## Background

The idea for this project emerged after watching the [When will it be done? Presentation by Daniel Vacanti].
In his presentation, Daniel shares results of different work policies by simulating the policies 
using a proprietary simulation application. Let's verify these experiments using open source tools!

Daniel has written out his ideas in two books; one of which inspired the name of this application:
_When will it be done?_ [Vacanti2000].

## License

The MIT License (MIT) [License]

Copyright (c) 2020 Marijn van der Zee

---

## References

 [CS50x Final Project Description]: https://cs50.harvard.edu/x/2020/project/
 [When will it be done? Presentation by Daniel Vacanti]: https://vimeo.com/239539858
 [Vacanti2009]: https://leanpub.com/whenwillitbedone
 [SimPy]: https://simpy.readthedocs.io/
 [License]: ./LICENSE