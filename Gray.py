import cv2
import color_tracker


def tracker_callback(t: color_tracker.ColorTracker):
    try:
        print(tracker.tracked_objects[0].id)
        print(tracker.tracked_objects[0].last_point)
        cv2.putText(t.debug_frame, str(tracker.tracked_objects[0].last_point), (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(t.debug_frame, "Siguiendo", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    except:
        cv2.putText(t.debug_frame, "No hay objetos", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        pass
    cv2.imshow("debug", t.debug_frame)
    cv2.waitKey(1)


tracker = color_tracker.ColorTracker(max_nb_of_objects=1, max_nb_of_points=20, debug=True)
tracker.set_tracking_callback(tracker_callback)

with color_tracker.WebCamera() as cam:
    # Define your custom Lower and Upper HSV values
    tracker.track(cam, [155, 103, 82], [178, 255, 255], max_skipped_frames=24 ,min_contour_area=100)