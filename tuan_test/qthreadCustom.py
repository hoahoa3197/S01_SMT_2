from PyQt6.QtCore import *
import traceback, sys

class WorkerSignals(QObject):
    # Signal Status ! of Worker
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(object)

class SDWorker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(SDWorker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        if 'progress_callback' in kwargs:
            self.kwargs['progress_callback'] = self.signals.progress

    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            print('Error CSWorker')
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done
            
    def stop(self):
        self._isRunning = False
        print('Stopped Now')