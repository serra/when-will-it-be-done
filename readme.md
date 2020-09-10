# When will it be done

> Strive to create something that outlives this course.
>
> -- [CS50x Final Project Description]

## Product Vision

Self-organizing development teams have are in control of the way they go about their work.
They are able to connect their way of working
to the needs of the people with a stake in their work.
While going about their work, they reflect and improve: there must be a better way!

The when-will-it-be-done app will allow development teams to 
quickly experiment with different ways to go about their work.
These experiments will allow teams to assess the effects of new work policies
*before* they choose to apply them -
after minutes of coding and simulation.

This app allows development teams to 
see the impact of micro-, everyday decisions in terms of whole-playing-field outcomes.

It does it in a way that appeals to developers: 

 1. fork this repo
 1. modify the models to reflect your team's work policies
 1. run a simulation
 1. learn from the simulation's output

## Product Specification

<details>
(Nothing here yet, deliberatley left blank.
Once we finish items from our product backlog, 
this specification will fill up.)
</details>

### Installation

Clone this repository. From your favourite command line interface, 
navigate to the root of the environment and start a pipenv shell:

```
pipenv shell
python ./examples/01/sprint.py
```

Sim away!

### How to use

## Backlogs

### Doing

 * [ ] Simulate a team with capacity-constrained skills, modelled as resources

### Product Backlog

 * [ ] Capture output of a simulation in a CFD
 * [ ] Simulate a Swarming Scrum Team
 * [ ] Explore ways to capture simulation output metrics
 * [ ] Simulate a siloed Kanban work group
 * [ ] Collect output metrics from wwibd
    * cycle time scatterplots
    * cycle time scatterplots with percentiles
    * flow efficiency
    * cycle time histograms
    * throughput
    * CFD
    * start & stop time per work item
 * [ ] Chapter 11 of [Vacanti2000] is a great description on how to get started wth process improvement; 
       it serves as a great way for modelling and simulating too.
 * [ ] Distill sample scenarios from [Vacanti2009]
 * [ ] Make a collection of interesting agile paradigms to confirm or to falsify
       (cross functional team, T-shaped team members, single piece flow, estimation,
       release early and often, swarming).
 * [ ] Simulate the effect of disruptions and various ways to handle them (e.g. expediting)
 * [ ] Experiment with pull policies (Fifo, , )
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