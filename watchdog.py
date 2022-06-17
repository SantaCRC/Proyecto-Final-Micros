import cv2
import color_tracker
import threading
import servos
import keyboard
def isInside(circle_x, circle_y, rad, x, y):
     # funcion que determina si un punto esta dentro de un circulo
    if ((x - circle_x) * (x - circle_x) +
        (y - circle_y) * (y - circle_y) <= rad * rad):
        return True;
    else:
        return False;

def tracker_callback(t: color_tracker.ColorTracker):
    try:
        print(tracker.tracked_objects[0].id)
        print(tracker.tracked_objects[0].last_point)
        cv2.putText(t.debug_frame, str(tracker.tracked_objects[0].last_point), (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        if isInside(320, 240, 75, tracker.tracked_objects[0].last_point[0], tracker.tracked_objects[0].last_point[1]):
            cv2.putText(t.debug_frame, "En la mira", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        else:
            threading.Thread(target=servos.main,args=(tracker.tracked_objects[0].last_point,)).start()
            cv2.putText(t.debug_frame, "Siguiendo", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    except:
        cv2.putText(t.debug_frame, "No hay objetos", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        pass
    cv2.circle(t.debug_frame, (320,240), 75, (255, 255, 255), 2)
    cv2.imshow("debug", t.debug_frame)
    cv2.waitKey(1)
    if keyboard.is_pressed('q'):
        cv2.destroyAllWindows() # cierra todas las ventanas

    

tracker = color_tracker.ColorTracker(max_nb_of_objects=1, max_nb_of_points=20, debug=True)
tracker.set_tracking_callback(tracker_callback)



def main(lower, upper):
    with color_tracker.WebCamera() as cam:
        # Define el color que se va a detectar
        tracker.track(cam, lower, upper, max_skipped_frames=24 ,min_contour_area=100)

if __name__ == '__main__':
    tracker = color_tracker.ColorTracker(max_nb_of_objects=1, max_nb_of_points=20, debug=True)
    tracker.set_tracking_callback(tracker_callback)
    main([155, 103, 82],[178, 255, 255])