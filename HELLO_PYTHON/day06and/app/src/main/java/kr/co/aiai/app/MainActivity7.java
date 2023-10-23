package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;


public class MainActivity7 extends AppCompatActivity {

    EditText et_first, et_last;
    TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main7);

        et_first = findViewById(R.id.et_first);
        et_last = findViewById(R.id.et_last);
        tv = findViewById(R.id.tv);
        Button btn = findViewById(R.id.btn);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();
            }
        });
    }

    public String getStar(int cnt){
        String ret = "";
        for(int i=0; i<cnt; i++){
            ret += "*";
        }
        ret += "\n";
        return ret;
    }

    public void myclick(){
        String f = et_first.getText().toString();
        String l = et_last.getText().toString();
        int ff = Integer.parseInt(f);
        int ll = Integer.parseInt(l);

        String txt = "";

        for(int i=ff; i<=ll; i++){
            txt += getStar(i);
        }


        tv.setText(txt);
    }
}