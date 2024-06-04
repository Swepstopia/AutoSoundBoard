#24/8/2014

#Important to note that if there is less than 20 files in the directory when running this script, the script will fail.

#This line messes up because python injects itself into it. Need to manually re-place it in the output java:
#getContentResolver().delete(uri, MediaStore.MediaColumns.DATA + "=\"" + k.getAbsolutePath() + "\"", null);
 
import os

#This method creates an array of all the filenames that are put into the soundNameString array
def soundNameString(soundNames):
	global soundNameString
	soundNameString = []
	x = 0
	for sound in soundNames:
		soundNameString.append("\"" + soundNames[x] + "\"")
		x+=1
		
def soundNameStringDEMO(soundNames):
	global soundNameStringDEMO
	soundNameStringDEMO = []
	for sound in range(0, 20):
		soundNameStringDEMO.append("\"" + soundNames[sound] + "\"")
		

#This method creates the soundIDs array
def soundIDs(soundNames):
	global soundIDs
	x = 0
	soundIDs = []
	for sound in soundNames:
		soundIDs.append("abc123R.raw." + soundNames[x] + "abc123")
		x+=1

def soundIDsDEMO(soundNames):
	global soundIDsDEMO
	soundIDsDEMO = []
	for sound in range(0, 20):
		soundIDsDEMO.append("abc123R.raw." + soundNames[sound] + "abc123")
		

		
#This method creates the btnIDs array
def btnIDs(soundNames):
	global btnIDs
	x = 0
	btnIDs = []
	for sound in soundNames:
		btnIDs.append("abc123R.id.b_" + soundNames[x] + "abc123")
		x+=1
		
def btnIDsDEMO(soundNames):
	global btnIDsDEMO
	btnIDsDEMO = []
	for sound in range(0, 20):
		btnIDsDEMO.append("abc123R.id.b_" + soundNames[sound] + "abc123")		
		


#Generate the buttons
def createButtons():
	global buttons
	buttons = []
	for number in range(0, len(files)):
		buttons.append("private Button B_" + str(number))

		
def createButtonsDEMO():
	global buttonsDEMO
	buttonsDEMO = []
	for number in range(0, 20):
		buttonsDEMO.append("private Button B_" + str(number))
		
		
def createMediaPlayers():
	global mediaPlayer
	mediaPlayer = []
	x = 0
	for number in range(0, len(files)):
		mediaPlayer.append("private MediaPlayer M_" + str(number))
		x += 1
		print mediaPlayer[x -1]
				
				
def createMediaPlayersDEMO():
	global mediaPlayerDEMO
	mediaPlayerDEMO = []
	for number in range(0, 20):
		mediaPlayerDEMO.append("private MediaPlayer M_" + str(number))				

		
def createMediaPlayerObjectArray():
	global mediaArrayObjects
	mediaArrayObjects = []
	for number in range(0, len(files)):
		mediaArrayObjects.append("abc123M_" + str(number) + "abc123")
		
def createMediaPlayerObjectArrayDEMO():
	global mediaArrayObjectsDEMO
	mediaArrayObjectsDEMO = []
	for number in range(0, 20):
		mediaArrayObjectsDEMO.append("abc123M_" + str(number) + "abc123")
	
def createButtonObjectArray():
	global buttonArrayObjects
	buttonArrayObjects = []
	for number in range(0, len(files)):
		buttonArrayObjects.append("abc123B_" + str(number) + "abc123")
		
def createButtonObjectArrayDEMO():
	global buttonArrayObjectsDEMO
	buttonArrayObjectsDEMO = []
	for number in range(0, 20):
		buttonArrayObjectsDEMO.append("abc123B_" + str(number) + "abc123")

def createFiles():
	global files
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	if "auto_code.py" in files: files.remove("auto_code.py")
	if "Main.txt" in files: files.remove("Main.txt")
	if "xml.txt" in files: files.remove("xml.txt")
	if "demo_main.txt" in files: files.remove("demo_main.txt")

#PROGRAM START
#Grab the list of files and store in an array
createFiles()

#Run the method to create the soundNameString array
soundNameString(files)
#Run the method to create the soundIDs array
soundIDs(files)
#Run the method to create the btnIDs array
btnIDs(files)

#Create the list of buttons
createButtons()

#Create the media player objects
createMediaPlayers()

#Create the mediaplayer array with the mediaPlayer objects
createMediaPlayerObjectArray()

#Create the button array with the button objects
createButtonObjectArray()


###############These methods are for the Demo file
##################################################
soundNameStringDEMO(files)
soundIDsDEMO(files)	
btnIDsDEMO(files)
createButtonsDEMO()
createMediaPlayersDEMO()
createMediaPlayerObjectArrayDEMO()
createButtonObjectArrayDEMO()


#Create and input the JavaCode
file = open("Main.txt", "w")

file.write("""import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

import android.support.v7.app.ActionBarActivity;
import android.content.ContentValues;
import android.content.Intent;
import android.media.MediaPlayer;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.ContextMenu;
import android.view.MenuItem;
import android.view.View;
import android.view.ContextMenu.ContextMenuInfo;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends ActionBarActivity {

""")


for num in range(0, len(files)):
	file.write("private Button B_" + str(num) + ";\n")

file.write("\n")

for num in range(0, len(files)):
	file.write("private MediaPlayer M_" + str(num) + ";\n")	

file.write(
"\nprivate final MediaPlayer sounds[] = " + str(mediaArrayObjects) + "\n" + "private final Button buttons[] = " + str(buttonArrayObjects) + "\n\n private final String soundNameString[] = " + str(soundNameString) + "\n\n private final int soundIDs[] = " + str(soundIDs) + "\n\n" + "private final int btnIDs[] = " + str(btnIDs) + """

String soundNames[];
int selected;

@Override
protected void onCreate(Bundle savedInstanceState) {
	// TODO Auto-generated method stub
	super.onCreate(savedInstanceState);
	setContentView(R.layout.activity_main);
		
	for(int x = 0; x < sounds.length; x++){
		sounds[x] = MediaPlayer.create(MainActivity.this, soundIDs[x]);
		buttons[x] = (Button) findViewById(btnIDs[x]);
		registerForContextMenu(buttons[x]);
	}
}

@Override
public void onCreateContextMenu(ContextMenu menu, View v,
	ContextMenuInfo menuInfo) {
	super.onCreateContextMenu(menu, v, menuInfo);
	menu.setHeaderTitle("Set as:");  
	   menu.add(0, v.getId(), 0, "Ringtone");
	   menu.add(0, v.getId(), 0, "SMS");
}
	
	
	
@Override
public boolean onContextItemSelected(MenuItem item) {	
	//Find the array location of item
	soundNames = new String[sounds.length];
	for(int x = 0; x < btnIDs.length; x++){
		soundNames[x] = "" + btnIDs[x];
	}
	selected = Arrays.asList(soundNames).indexOf("" + item.getItemId());
				
	if(item.getTitle().equals("Ringtone")){function1(item.getItemId());}  
		else if(item.getTitle().equals("SMS")){function2(item.getItemId());}  
		else {return false;}  
		return true;  
}
		
	
public void function1(int id){
	if 
	(savering(soundIDs[selected])){   
	// Code if successful   
	Toast.makeText(this, "Saved as Ringtone", Toast.LENGTH_SHORT).show(); 
	}           
	else           
		{ 
		// Code if unsuccessful   
	     Toast.makeText(this, "Failed - Check your SDCard", Toast.LENGTH_SHORT).show();
	    }
}//end function1
		
		
	
public void function2(int id){	
	if 
	(savenot(soundIDs[selected])){   
	// Code if successful   
	Toast.makeText(this, "Saved as Notification", Toast.LENGTH_SHORT).show(); 
	}           
	else           
	   { 
	// Code if unsuccessful   
	Toast.makeText(this, "Failed - Check your SDCard", Toast.LENGTH_SHORT).show(); 
	}
}//end Function2
		
	
public boolean savering(int ressound){
	byte[] buffer=null;
	InputStream fIn = getBaseContext().getResources().openRawResource(ressound);
	int size=0; 
	
	try {
		size = fIn.available();   
	    buffer = new byte[size];   
	    fIn.read(buffer);   
	    fIn.close(); 
	    } catch (IOException e) { 
	// TODO Auto-generated catch block   
	    return false;      } 

	    String path="/sdcard/media/audio/ringtones/";
	    String filename=soundNameString[selected]; 

	    boolean exists = (new File(path)).exists();   
	    if (!exists){new File(path).mkdirs();}   
			FileOutputStream save;
			try { 
				save = new FileOutputStream(path+filename);   
				save.write(buffer);   
				save.flush();   
				save.close();   
	     } catch (FileNotFoundException e) { 
	      // TODO Auto-generated catch block   
	      return false;  
	     } catch (IOException e) {
	      // TODO Auto-generated catch block   
	      return false;
	     }
	     sendBroadcast(new Intent(Intent.ACTION_MEDIA_SCANNER_SCAN_FILE, Uri.parse("file://"+path+filename))); 

	     File k = new File(path, filename);   
	     ContentValues values = new ContentValues();   
	     values.put(MediaStore.MediaColumns.DATA, k.getAbsolutePath());   
	     values.put(MediaStore.MediaColumns.TITLE, soundNameString[selected] + " Ringtone");   
	     values.put(MediaStore.MediaColumns.MIME_TYPE, "audio/ogg");   
	     values.put(MediaStore.Audio.Media.ARTIST, "SoundBoard Sounds ");   
	     values.put(MediaStore.Audio.Media.IS_RINGTONE, true);   
	     values.put(MediaStore.Audio.Media.IS_NOTIFICATION, true);   
	     values.put(MediaStore.Audio.Media.IS_ALARM, true);   
	     values.put(MediaStore.Audio.Media.IS_MUSIC, false);    

	     //Insert it into the database
	     Uri uri = MediaStore.Audio.Media.getContentUriForPath(k.getAbsolutePath());
	     getContentResolver().delete(uri, MediaStore.MediaColumns.DATA + "=\"" + k.getAbsolutePath() + "\"", null);
	     Uri newUri = getContentResolver().insert(uri, values);
	     RingtoneManager.setActualDefaultRingtoneUri(MainActivity.this,RingtoneManager.TYPE_RINGTONE,newUri);

	     return true; 
}// end savering

	//Save in Notification Folder

	    public boolean savenot(int ressound){
	     byte[] buffer=null;
	     InputStream fIn = getBaseContext().getResources().openRawResource(ressound);
	     int size=0; 

	     try {
	       size = fIn.available();   
	       buffer = new byte[size];   
	       fIn.read(buffer);   
	       fIn.close(); 
	     } catch (IOException e) { 
	      // TODO Auto-generated catch block   
	      return false;      } 

	     String path="/sdcard/media/audio/notifications/";
	     String filename=soundNameString[selected]; 

	     boolean exists = (new File(path)).exists();   
	     if (!exists){new File(path).mkdirs();}   

	     FileOutputStream save;
	     try { 
	      save = new FileOutputStream(path+filename);   
	      save.write(buffer);   
	      save.flush();   
	      save.close();   
	     } catch (FileNotFoundException e) { 
	      // TODO Auto-generated catch block   
	      return false;  
	     } catch (IOException e) {
	      // TODO Auto-generated catch block   
	      return false;
	     }
	     sendBroadcast(new Intent(Intent.ACTION_MEDIA_SCANNER_SCAN_FILE, Uri.parse("file://"+path+filename))); 

	     File k = new File(path, filename);   
	     ContentValues values = new ContentValues();   
	     values.put(MediaStore.MediaColumns.DATA, k.getAbsolutePath());   
	     values.put(MediaStore.MediaColumns.TITLE, soundNameString[selected] + " Notification");   
	     values.put(MediaStore.MediaColumns.MIME_TYPE, "audio/ogg");   
	     values.put(MediaStore.Audio.Media.ARTIST, "SoundBoard Sounds ");   
	     values.put(MediaStore.Audio.Media.IS_RINGTONE, true);   
	     values.put(MediaStore.Audio.Media.IS_NOTIFICATION, true);   
	     values.put(MediaStore.Audio.Media.IS_ALARM, true);   
	     values.put(MediaStore.Audio.Media.IS_MUSIC, false);    

	     //Insert it into the database
	     Uri uri = MediaStore.Audio.Media.getContentUriForPath(k.getAbsolutePath());
	     getContentResolver().delete(uri, MediaStore.MediaColumns.DATA + "=\"" + k.getAbsolutePath() + "\"", null);
	     Uri newUri = getContentResolver().insert(uri, values);
	     RingtoneManager.setActualDefaultRingtoneUri(MainActivity.this,RingtoneManager.TYPE_NOTIFICATION,newUri);
	    	      			
	     return true; 
	    }//end saveNot
	""")	

for line in range(0, len(files)):
	file.write( """\n	public void onClick""" + str(line) + """(View v){
		for(int x = 0; x < sounds.length; x++){
			sounds[x].release();
		}
		sounds[""" + str(line) + """] = MediaPlayer.create(MainActivity.this, soundIDs[""" + str(line) + """]);
		sounds[""" + str(line) + """].start();
	} \n""")
file.close()

file = open("Main.txt", "a")

file.write("""
	@Override
	protected void onPause() {
		super.onPause();
		for(int x = 0; x < sounds.length; x++){
			sounds[x].release();
		}	
	}
}""")
file.close()

#######Generate the XML file########
xml_file = open("xml.txt", "w")

xml_file.write("""
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#000000"
    android:orientation="vertical" >

###################################################
###############PLACE IMAGE CODE HERE####################
###################################################

<ScrollView
        android:id="@+id/scrollView1"
        android:layout_width="fill_parent"
        android:layout_height="320dp"
        android:layout_alignParentBottom="true"
        android:layout_alignParentLeft="true"
        android:layout_below="@+id/imageView1" >

        <LinearLayout
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical" >""")
			
for line in range(0, len(files)):
		xml_file.write("""<Button
                android:id="@+id/b_""" + str(soundNameString[line]) + """"
                android:layout_width="match_parent"
                android:layout_height="46dp"
                android:layout_alignParentLeft="true"
                android:layout_alignParentRight="true"
                android:layout_below="@+id/imageView1"
                android:background="#000000"
                android:onClick="onClick""" + str(line) + "\"""""
                android:text=""""\"" + str(soundNameString[line]) + "\"""""
                android:textColor="#FFFFFF" />
				
				
				""")
xml_file.write("""</LinearLayout>
    </ScrollView>

</RelativeLayout>""")

xml_file.close()


########################DEMO FILE########################
#########################################################
#########################################################



demo_main = open("demo_main.txt", "w")

demo_main.write("""import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

import android.text.SpannableString;
import android.support.v7.app.ActionBarActivity;
import android.content.ContentValues;
import android.content.Intent;
import android.media.MediaPlayer;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.ContextMenu;
import android.view.MenuItem;
import android.view.View;
import android.view.ContextMenu.ContextMenuInfo;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends ActionBarActivity {

""")

for num in range(0, 20):
	demo_main.write("private Button B_" + str(num) + ";\n")

demo_main.write("\n")

for num in range(0, 20):
	demo_main.write("private MediaPlayer M_" + str(num) + ";\n")

demo_main.write(
"\nprivate final MediaPlayer sounds[] = " + str(mediaArrayObjectsDEMO) + "\n" + "private final Button buttons[] = " + str(buttonArrayObjectsDEMO) + "\n\n private final String soundNameString[] = " + str(soundNameStringDEMO) + "\n\n private final int soundIDs[] = " + str(soundIDsDEMO) + "\n\n" + "private final int btnIDs[] = " + str(btnIDsDEMO) + """

String soundNames[];
int selected;

@Override
protected void onCreate(Bundle savedInstanceState) {
	// TODO Auto-generated method stub
	super.onCreate(savedInstanceState);
	setContentView(R.layout.activity_main);
		
	for(int x = 0; x < sounds.length; x++){
		sounds[x] = MediaPlayer.create(MainActivity.this, soundIDs[x]);
		buttons[x] = (Button) findViewById(btnIDs[x]);
		registerForContextMenu(buttons[x]);
	}
}

@Override
public void onCreateContextMenu(ContextMenu menu, View v,
	ContextMenuInfo menuInfo) {
	super.onCreateContextMenu(menu, v, menuInfo);
	menu.setHeaderTitle("Set as:");  
	   menu.add(0, v.getId(), 0, "Ringtone");
	   menu.add(0, v.getId(), 0, "SMS");
}
	
	
	
@Override
public boolean onContextItemSelected(MenuItem item) {	
	//Find the array location of item
	soundNames = new String[sounds.length];
	for(int x = 0; x < btnIDs.length; x++){
		soundNames[x] = "" + btnIDs[x];
	}
	selected = Arrays.asList(soundNames).indexOf("" + item.getItemId());
				
	if(item.getTitle().equals("Ringtone")){function1(item.getItemId());}  
		else if(item.getTitle().equals("SMS")){function2(item.getItemId());}  
		else {return false;}  
		return true;  
}
		
	
public void function1(int id){
	if 
	(savering(soundIDs[selected])){   
	// Code if successful   
	Toast.makeText(this, "Saved as Ringtone", Toast.LENGTH_SHORT).show(); 
	}           
	else           
		{ 
		// Code if unsuccessful   
	     Toast.makeText(this, "Failed - Check your SDCard", Toast.LENGTH_SHORT).show();
	    }
}//end function1
		
		
	
public void function2(int id){	
	if 
	(savenot(soundIDs[selected])){   
	// Code if successful   
	Toast.makeText(this, "Saved as Notification", Toast.LENGTH_SHORT).show(); 
	}           
	else           
	   { 
	// Code if unsuccessful   
	Toast.makeText(this, "Failed - Check your SDCard", Toast.LENGTH_SHORT).show(); 
	}
}//end Function2
		
	
public boolean savering(int ressound){
	byte[] buffer=null;
	InputStream fIn = getBaseContext().getResources().openRawResource(ressound);
	int size=0; 
	
	try {
		size = fIn.available();   
	    buffer = new byte[size];   
	    fIn.read(buffer);   
	    fIn.close(); 
	    } catch (IOException e) { 
	// TODO Auto-generated catch block   
	    return false;      } 

	    String path="/sdcard/media/audio/ringtones/";
	    String filename=soundNameString[selected]; 

	    boolean exists = (new File(path)).exists();   
	    if (!exists){new File(path).mkdirs();}   
			FileOutputStream save;
			try { 
				save = new FileOutputStream(path+filename);   
				save.write(buffer);   
				save.flush();   
				save.close();   
	     } catch (FileNotFoundException e) { 
	      // TODO Auto-generated catch block   
	      return false;  
	     } catch (IOException e) {
	      // TODO Auto-generated catch block   
	      return false;
	     }
	     sendBroadcast(new Intent(Intent.ACTION_MEDIA_SCANNER_SCAN_FILE, Uri.parse("file://"+path+filename))); 

	     File k = new File(path, filename);   
	     ContentValues values = new ContentValues();   
	     values.put(MediaStore.MediaColumns.DATA, k.getAbsolutePath());   
	     values.put(MediaStore.MediaColumns.TITLE, soundNameString[selected] + " Ringtone");   
	     values.put(MediaStore.MediaColumns.MIME_TYPE, "audio/ogg");   
	     values.put(MediaStore.Audio.Media.ARTIST, "SoundBoard Sounds ");   
	     values.put(MediaStore.Audio.Media.IS_RINGTONE, true);   
	     values.put(MediaStore.Audio.Media.IS_NOTIFICATION, true);   
	     values.put(MediaStore.Audio.Media.IS_ALARM, true);   
	     values.put(MediaStore.Audio.Media.IS_MUSIC, false);    

	     //Insert it into the database
	     Uri uri = MediaStore.Audio.Media.getContentUriForPath(k.getAbsolutePath());
	     getContentResolver().delete(uri, MediaStore.MediaColumns.DATA + "=\"" + k.getAbsolutePath() + "\"", null);
	     Uri newUri = getContentResolver().insert(uri, values);
	     RingtoneManager.setActualDefaultRingtoneUri(MainActivity.this,RingtoneManager.TYPE_RINGTONE,newUri);

	     return true; 
}// end savering

	//Save in Notification Folder

	    public boolean savenot(int ressound){
	     byte[] buffer=null;
	     InputStream fIn = getBaseContext().getResources().openRawResource(ressound);
	     int size=0; 

	     try {
	       size = fIn.available();   
	       buffer = new byte[size];   
	       fIn.read(buffer);   
	       fIn.close(); 
	     } catch (IOException e) { 
	      // TODO Auto-generated catch block   
	      return false;      } 

	     String path="/sdcard/media/audio/notifications/";
	     String filename=soundNameString[selected]; 

	     boolean exists = (new File(path)).exists();   
	     if (!exists){new File(path).mkdirs();}   

	     FileOutputStream save;
	     try { 
	      save = new FileOutputStream(path+filename);   
	      save.write(buffer);   
	      save.flush();   
	      save.close();   
	     } catch (FileNotFoundException e) { 
	      // TODO Auto-generated catch block   
	      return false;  
	     } catch (IOException e) {
	      // TODO Auto-generated catch block   
	      return false;
	     }
	     sendBroadcast(new Intent(Intent.ACTION_MEDIA_SCANNER_SCAN_FILE, Uri.parse("file://"+path+filename))); 

	     File k = new File(path, filename);   
	     ContentValues values = new ContentValues();   
	     values.put(MediaStore.MediaColumns.DATA, k.getAbsolutePath());   
	     values.put(MediaStore.MediaColumns.TITLE, soundNameString[selected] + " Notification");   
	     values.put(MediaStore.MediaColumns.MIME_TYPE, "audio/ogg");   
	     values.put(MediaStore.Audio.Media.ARTIST, "SoundBoard Sounds ");   
	     values.put(MediaStore.Audio.Media.IS_RINGTONE, true);   
	     values.put(MediaStore.Audio.Media.IS_NOTIFICATION, true);   
	     values.put(MediaStore.Audio.Media.IS_ALARM, true);   
	     values.put(MediaStore.Audio.Media.IS_MUSIC, false);    

	     //Insert it into the database
	     Uri uri = MediaStore.Audio.Media.getContentUriForPath(k.getAbsolutePath());
	     getContentResolver().delete(uri, MediaStore.MediaColumns.DATA + "=\"" + k.getAbsolutePath() + "\"", null);
	     Uri newUri = getContentResolver().insert(uri, values);
	     RingtoneManager.setActualDefaultRingtoneUri(MainActivity.this,RingtoneManager.TYPE_NOTIFICATION,newUri);
	    	      			
	     return true; 
	    }//end saveNot
	""")

for line in range(0, 20):
	demo_main.write( """\n	public void onClick""" + str(line) + """(View v){
		for(int x = 0; x < sounds.length; x++){
			sounds[x].release();
		}
		sounds[""" + str(line) + """] = MediaPlayer.create(MainActivity.this, soundIDs[""" + str(line) + """]);
		sounds[""" + str(line) + """].start();
	} \n""")
	
	
for line in range(20, len(files)):
	demo_main.write( """\n	public void onClick""" + str(line) + """(View v){
			for(int x = 0; x < sounds.length; x++){
			sounds[x].release();
			}
			openOptionsMySiteDialog();
	} \n""")
	
demo_main.write("""//This method is the dialog box for the clickable link to the paid version of the app. 
	 private void openOptionsMySiteDialog(){
	 final SpannableString stMyWeb = new SpannableString("http://swepsy.bounceme.net/");
	 final TextView message = new TextView(getBaseContext());
	 message.setText("Upgrade to full version?");
	    Linkify.addLinks(stMyWeb, Linkify.ALL);
	    final AlertDialog aboutDialog = new AlertDialog.Builder(MainActivity.this).setMessage(stMyWeb).setTitle("Upgrade to full version?").setIcon(android.R.drawable.ic_dialog_info).setPositiveButton("Dismiss", new DialogInterface.OnClickListener() {
		 @Override
		 public void onClick(DialogInterface dialog, int which) {}}).create();
		   aboutDialog.show();
		((TextView)aboutDialog.findViewById(android.R.id.message))
		 .setMovementMethod(LinkMovementMethod.getInstance());
		}
		
		@Override
	protected void onPause() {
		super.onPause();
		for(int x = 0; x < sounds.length; x++){
			sounds[x].release();
		}	
	}
		
		
}""")	
demo_main.close()
