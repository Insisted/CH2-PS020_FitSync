package com.example.CH2_PS020.fitsync

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.MenuItem
import androidx.fragment.app.Fragment
import com.example.CH2_PS020.fitsync.databinding.ActivityMainBinding
import com.example.CH2_PS020.fitsync.ui.account.AccountFragment
import com.example.CH2_PS020.fitsync.ui.home.HomeFragment
import com.example.CH2_PS020.fitsync.ui.tracker.TrackerFragment
import com.example.CH2_PS020.fitsync.ui.workout.WorkoutFragment

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        val homeFragment = HomeFragment()
        val workoutFragment = WorkoutFragment()
        val trackerFragment = TrackerFragment()
        val accountFragment = AccountFragment()
        setFragment(homeFragment)
        binding.bottomNavigationView.setOnItemSelectedListener {
            when(it.itemId){
                R.id.menu_home    ->setFragment(homeFragment)
                R.id.menu_workout -> setFragment(workoutFragment)
                R.id.menu_tracker -> setFragment(trackerFragment)
                R.id.menu_account -> setFragment(accountFragment)
                else -> false
            }
        }
    }



    private fun setFragment(fragment:Fragment):Boolean {
        supportFragmentManager
            .beginTransaction()
            .replace(binding.frameLayout.id, fragment)
            .commit()

        return true
    }
}