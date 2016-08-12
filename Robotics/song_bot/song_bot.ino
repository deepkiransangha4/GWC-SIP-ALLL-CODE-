int pin = 5;

// One octave of notes between A4 and A5
int note_E4 = 329.6;
int note_G4 = 392;
int note_A4 = 440;
int note_As4 = 466; int note_Bb4 = note_As4;
int note_B4 = 494;
int note_C5 = 523;
int note_Cs5 = 554; int note_Db5 = note_Cs5;
int note_D5 = 587;
int note_Ds5 = 622; int note_Eb5 = note_Ds5;
int note_E5 = 659;
int note_F5 = 698;
int note_Fs5 = 740; int note_Gb5 = note_Fs5;
int note_G5 = 784;
int note_Gs5 = 830; int note_Ab5 = note_Gs5;

int note_A5 = note_A4 * 2;
int note_As5 = note_As4 * 2; int note_Bb5 = note_As5;
int note_B5 = note_B4 * 2;

int note_rest = -1;

// note lengths defined here
long whole_note = 1600; // change tempo by changing duration of one measure
long half_note = whole_note / 2;
long quarter_note = whole_note / 4;
long eighth_note = whole_note / 8;
long sixteenth_note = whole_note / 16;
long dotted_quarter_note = quarter_note + eighth_note;
long dotted_half_note = quarter_note + half_note; 

// WRITE YOUR SONG HERE

int song[14][2] = {{note_E4, quarter_note}, {note_A4, dotted_quarter_note}, {note_C5, eighth_note},{note_B4,quarter_note},{note_A4, half_note}, {note_E5,quarter_note},
{note_D5, dotted_quarter_note}, {note_B4, dotted_half_note},{note_A4, quarter_note},{note_C5, quarter_note}, {note_B4, quarter_note}, 
{note_G4, half_note}, {note_Bb4, quarter_note}, {note_E4,whole_note}}; 

// if you want there to be silence between notes,
//   staccato should be true
bool staccato = true;

void setup() {
  //pinMode(PIEZOPIN, OUTPUT);
  pinMode(pin, OUTPUT);
}

void loop() {
  
  //PLAY YOUR SONG HERE
  int i = 0;
  for (i; i < 14; i++) {
    tone(pin, song[i][0]);
    delay(song[i][1]); // delay for the duration of your note type
  }
  
}
