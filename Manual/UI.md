# 03 Tracking UI and Clustering UI

This interface is browser-based. We recommend using `Google Chrome` as the browser. 

Pre-installed Python3 is required since this package includes Python scripts.

## Running
### By GUI (recommended for non-cs users)
<div align="center">
    <img src="media/main_ui/main_result.png", width="500" alt><br>
    <img src="media/main_ui/vis_results.png", width="500" alt><br>
    AlphaTracker GUI open WebUI page
</div>

Please visit our video tutorial for WebUI at [YouTube](https://youtu.be/9Ksb04s8mm4).

### Or by command line
Change your working directory to [UI/](../UI) by running `cd ./UI`. Then run `python server.py` in command window in the unzipped folder. 

<br>
    

## Tracking UI

A window should appear in the user's browser. Then click `html/`. From there, select a program you want to run. `cluster.html` is the Cluster UI and `curate.html` is the Tracking UI.

<img src="media/html.jpg" width = "400" /><br><img src="media/window.png" width = "400" />



### Import data


- Click the first `Click Here` button to upload the track result JSON file. For example, [alphapose-results-forvis-tracked.json](../Tracking/AlphaTracker/track_result/alphapose-results-forvis-tracked.json)

- Click the second `Click Here`button to upload the original video. For example, [demo.mp4](../Tracking/AlphaTracker/data/demo.mp4)

- Specify the frame rate of the imported video. *The default frame rate value is* `25.0`.

    <img src = "media/1.png" width = "400">

 <br>

### User interface

The functions of each element in the toolbar is explained by the numerical order shown in the figure.

<img src = "media/Curate.png" width = "1000" >



#### I. Navigation Bar

    - 1.1 Tracking: Link to the Curate UI.
    - 1.2 Behavior: Link to the Cluster UI.
    - 1.3 Help: Link to the Operation Manual.
    - 1.4 Export: Saves the current clip information as a local `.json` file.
    - 1.5 New Session: Prompts user to import new files and start a new session. **Beware:** If the user chooses to create a new session, all unsaved progress will be lost.
    - 1.6 Undo Button
    - 1.7 Redo Button

#### II. Operation Area
    - 2.1 Video Player: Dots of different color groups represents skeletal points of an individual identity. Such dots can be directly interacted with by simply dragging with the cursor to a new location.
    - 2.2 Jump To: Jump to a specific frame of the video.
    - 2.3 Curate: Curates an interval designated by function 3.5.
    - 2.4 Reassign Identity
    - 2.5 Operation Log
    - 2.6 Real-time Strip Line Update On/Off: Due to existing play-back performance issues of the CanvasJS API, the real-time strip line update is by default set to off. The action of turning on real-time update while working with long videos is strongly discouraged since it will slow down your playback perfomance.

####  III. Toolbar
    - 3.1 Play Button
    - 3.2 Time/Frame Position
    - 3.3 Frame Control: By clicking the corresponding button, the user can fast forward/roll back the video by a single frame.
    - 3.4 Second Control: By clicking the corresponding button, the user can fast forward/roll back the video by a single second.
    - 3.5 Set Interval: IN button designates the start of the interval while the OUT button designates the end.
    - 3.6 Playback Speed

#### IV. Progress Bar and Line Chart
    - 4.1 Progress Bar
    - 4.2 Line Chart&View Options: By clicking the text-box under identity tags, a drop-down menu will appear and let the user to choose from view options listed below:
        - 4.2.1 Box: As shown in the figure below.
        - 4.2.2 Point 1-4: Views the individual dots of an identity. The point score is hidden by default, the user can view the score by interacting with the chart legends.
        - 4.3.3 Score

<br>

##  Cluster UI

### Import Data
To  import data from Alphatracker clustering, follow the instructions shown on corresponding pop-ups.

- Step 1:  Upload the JSON file that contains the clip information. For example, [clips_info.json](../BehavioralClustering/data_for_ui_1/clips_info.json)

    <img src = "media/4.png" width = 400>


- Step 2: Click the `Import` button and upload the original video. Then specify the frame rate of the imported video. *The default frame rate value is* `30`.

    <img src = "media/5.png" width = 400>


- Step 3: Upload the JSON file that contains the cluster tree information. For example, [Z_all_twoMice.json](../BehavioralClustering/data_for_ui_1/Z_all_twoMice.json)

    <img src = "media/6.png" width = 400>

<br>

### User interface


The functions of each element in the toolbar is explained by the numerical order shown in the figure.

<img src = "media/Cluster.png">


#### I. Navigation Bar
            - 1.1 Tracking: Link to the Curate UI.
            - 1.2 Behavior: Link to the Cluster UI.
            - 1.3 Help: Link to the Operation Manual.
            - 1.4 Export: Saves the current dendrogram as a local `.json` file.
            - 1.5 New Session: Prompts user to upload new files and start a new session. **Beware:** If the user chooses to create a new session, all unsaved progress will be lost.
            - 1.6 Undo Button
            - 1.7 Redo Button

#### II. Operation Area
            - 2.1 Video Player
            - 2.2 Dendrogram: Displays the content of the uploaded dendrogram description     file. Double-clicking a node(be it clip or cluster) would highlight all the frames contained in the node.
                - 2.2.1 Right Click Menu
                    - 2.2.1.1 Move: Place the current cluster or clip node under the targeted cluster. <center><img src = "media/9.png" style="width: 60%;margin: 10px"></center>
                    - 2.2.1.2 Rename: Rename the current cluster. <center><img src = "media/10.png" style="width: 60%;margin: 10px"></center>
                    - 2.2.1.3 Delete: Delete currently selected node _while preserving its sub-nodes_.
                    - 2.2.1.4 Delete Subtree: Delete currently selected node _along with any of its sub-nodes_.
                - 2.2.2 `+/-`: Expand/Collapse
            - 2.3 Jump To: If the input is left blank and
            - 2.4 Merge: By designating two clip/cluster numbers, the selected nodes shall be merged. Such operation can only be applied to nodes of the same level.
            - 2.5 Operation Log
#### III. Toolbar
            - 3.1 Play Button
            - 3.2 Time/Frame Position
            - 3.3 Frame Control: By clicking the corresponding button, the user can fast forward/roll back the video by a single frame.
            - 3.4 Second Control: By clicking the corresponding button, the user can fast forward/roll back the video by a single second.
            - 3.5 Playback Speed
            - 3.6 Video Selection: For choosing video from imported files to show on the video player.
            - 3.7 Level Selection: Expand/collapse the dendrogram to a specified level.
            - 3.8 Current Clip Number
#### IV. Progress Bar and Scatterplot
            - 4.1 Progress Bar
            - 4.2 Scatterplot: The vertical axis represents clip number while the horizontal axes represents frame number. Any highlighted clips will be tinted cyan for easy observation.
