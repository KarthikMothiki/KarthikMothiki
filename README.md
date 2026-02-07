<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:22D3EE,100:06b6d4&height=120&section=header)

<pre>
<span style="color:#22D3EE">
██╗  ██╗ █████╗ ██████╗ ████████╗ ██╗  ██╗ ██╗ ██╗  ██╗
██║ ██╔╝██╔══██╗██╔══██╗╚══██╔══╝ ██║  ██║ ██║ ██║ ██╔╝
█████╔╝ ███████║██████╔╝   ██║    ███████║ ██║ █████╔╝ 
██╔═██╗ ██╔══██║██╔══██╗   ██║    ██╔══██║ ██║ ██╔═██╗ 
██║  ██╗██║  ██║██║  ██║   ██║    ██║  ██║ ██║ ██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═╝
</span>
<span style="color:#A855F7">
███╗   ███╗ ██████╗ ████████╗ ██╗  ██╗ ██╗ ██╗  ██╗ ██╗
████╗ ████║██╔═══██╗╚══██╔══╝ ██║  ██║ ██║ ██║ ██╔╝ ██║
██╔████╔██║██║   ██║   ██║    ███████║ ██║ █████╔╝  ██║
██║╚██╔╝██║██║   ██║   ██║    ██╔══██║ ██║ ██╔═██╗  ██║
██║ ╚═╝ ██║╚██████╔╝   ██║    ██║  ██║ ██║ ██║  ██╗ ██║
╚═╝     ╚═╝ ╚═════╝    ╚═╝    ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═╝ ╚═╝
</span>
<span style="color:#22C55E">
MECHATRONICS · AUTONOMOUS ROBOTS
</span>
</pre>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=3000&pause=1000&color=22D3EE&center=true&vCenter=true&width=750&lines=Production-Grade+Autonomous+Systems;C%2B%2B17+%C2%B7+ROS+2+%C2%B7+Real-Time+%C2%B7+Embedded;Machines+That+Perceive%2C+Reason%2C+and+Act)](https://git.io/typing-svg)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karthikmothiki/)
[![Email](https://img.shields.io/badge/Email-000000?style=flat&logo=gmail&logoColor=white)](mailto:karthik1111mothiki@gmail.com)
[![Medium](https://img.shields.io/badge/Medium-000000?style=flat&logo=medium&logoColor=white)](https://karthik-mothiki.medium.com/)
&nbsp;&nbsp;
![](https://komarev.com/ghpvc/?username=KarthikMothiki&style=flat&color=22D3EE&label=visitors)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   CALLSIGN....... Karthik Mothiki                                    ║
║   ROLE........... Robotics Software Engineer                         ║
║   CORE MODE...... AUTONOMOUS · REAL-TIME · FAIL-AWARE · PRODUCTION   ║
║   PRIMARY STACK.. C++17 | ROS 2 | Matlab | Control | Hardware        ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

</div>



I architect and ship **production-grade robotics software**—from bare-metal firmware to high-level behavior orchestration in ROS 2. My systems bridge hardware and intelligent autonomy for **consumer  robots**, built with a systems-engineering mindset where reliability isn't negotiable.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🏗️ System Architecture

```
╭────────────────────── SYSTEM ARCHITECTURE ──────────────────────╮
│                                                                 │
│   [ CAM ]──┐                                                    │
│   [ IMU ]──┼──▶  SENSOR FUSION  ──▶  PERCEPTION BUS             │
│   [ ENC ]──┘                     (POSE · STATE · VISION)        │
│                                                                 │
│              ┌──────────── DECISION FABRIC ────────────┐        │
│              │  BT · TASKS · MODES · FAILOVER          │        │
│              └──────────────────┬──────────────────────┘        │
│                                 ▼                               │
│                  REAL-TIME CONTROL LOOPS (kHz)                  │
│           TORQUE · VELOCITY · POSITION · LIMIT LOGIC            │
│                                 │                               │
│                                 ▼                               │
│                   PHYSICAL WORLD INTERFACE                      │
│                 MOTION · FORCE · ALIGNMENT                      │
│                                                                 │
╰─────────────────────────────────────────────────────────────────╯
```

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🔧 Capability Matrix

<div align="center">

| | Domain | Stack |
|:---:|:---|:---|
| ▣ | **Modern C++** | C++17 · Lock-free & deterministic design |
| ▣ | **ROS 2** | Executors · Lifecycle · Services · Large graph orchestration |
| ▣ | **Motor Control** | ODrive-class · Steppers · Torque & position loops |
| ▣ | **Vision Pipelines** | Capture → Encode → Stream → Inference |
| ▣ | **Sensor Fusion** | IMU calibration · Encoder truthing · Pose estimation |
| ▣ | **Behavior & Planning** | Behavior Trees · Nav2 · Task schedulers |
| ▣ | **Simulation** | MATLAB · Simulink · Gazebo · RViz2 |
| ▣ | **Hardware** | UART · I2C · SPI · CAN · PWM · ESP32 · Arduino |

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## ⚙️ Engineering Doctrine

```
───────────────────────────────────────────────────────────────
  ▸ Reality is the primary test environment
  ▸ Latency is a liability
  ▸ Undefined behavior is a failure, not a bug
  ▸ Every control loop must explain itself
  ▸ If recovery is not designed, the system is unfinished
───────────────────────────────────────────────────────────────
```

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 📊 Analytics

<div align="center">

<img height="160" src="https://github-readme-stats.vercel.app/api?username=KarthikMothiki&show_icons=true&theme=transparent&hide_border=true&title_color=22D3EE&icon_color=22D3EE&text_color=ffffff&bg_color=00000000" />
<img height="160" src="https://github-profile-trophy.vercel.app/?username=KarthikMothiki&theme=darkhub" />
<img height="160" src="https://github-readme-streak-stats.herokuapp.com/?user=KarthikMothiki&theme=transparent&hide_border=true&ring=22D3EE&fire=22D3EE&currStreakLabel=22D3EE&sideLabels=ffffff&currStreakNum=ffffff&sideNums=ffffff&dates=888888&background=00000000" />

<br><br>

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=KarthikMothiki&custom_title=&bg_color=00000000&color=22D3EE&line=22D3EE&point=ffffff&area=true&area_color=22D3EE&hide_border=true)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🚀 Featured Work

<div align="center">

[![Home Automation](https://github-readme-stats.vercel.app/api/pin/?username=KarthikMothiki&repo=Basic-Home-Automation&theme=transparent&hide_border=true&title_color=22D3EE&icon_color=22D3EE&text_color=ffffff&bg_color=00000000)](https://github.com/KarthikMothiki/Basic-Home-Automation)
[![Jarvis](https://github-readme-stats.vercel.app/api/pin/?username=KarthikMothiki&repo=Jarvis&theme=transparent&hide_border=true&title_color=22D3EE&icon_color=22D3EE&text_color=ffffff&bg_color=00000000)](https://github.com/KarthikMothiki/Jarvis)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 📬 Connect

<div align="center">

```
╭──────────────────────────────────────────────────────────────────╮
│                                                                  │
│   📧  karthik1111mothiki@gmail.com                               │
│   💼  linkedin.com/in/karthikmothiki                             │
│                                                                  │
│   Open to collaborations in autonomous systems, ROS 2,           │
│   and embedded robotics.                                         │
│                                                                  │
╰──────────────────────────────────────────────────────────────────╯
```

[![LinkedIn](https://img.shields.io/badge/Let's_Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karthikmothiki/)
[![Email](https://img.shields.io/badge/Email_Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:karthik1111mothiki@gmail.com)

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" alt="Snake animation" />
</p>

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:22D3EE,100:06b6d4&height=100&section=footer)

```
FORWARD DECLARATION
───────────────────
The future is not simulated.
It is embedded, calibrated, and deployed—
one control loop at a time.
```

</div>
